"""Minimal reader/writer for UE4 .locres (versions 0-3)."""
import struct

MAGIC = bytes.fromhex("0E147475674A03FC4A15909DC3377F1B")


class Reader:
    def __init__(self, data):
        self.d = data
        self.p = 0

    def u8(self):
        v = self.d[self.p]
        self.p += 1
        return v

    def i32(self):
        v = struct.unpack_from("<i", self.d, self.p)[0]
        self.p += 4
        return v

    def u32(self):
        v = struct.unpack_from("<I", self.d, self.p)[0]
        self.p += 4
        return v

    def i64(self):
        v = struct.unpack_from("<q", self.d, self.p)[0]
        self.p += 8
        return v

    def fstr(self):
        n = self.i32()
        if n == 0:
            return ""
        if n < 0:
            n = -n
            s = self.d[self.p:self.p + n * 2].decode("utf-16-le")
            self.p += n * 2
        else:
            s = self.d[self.p:self.p + n].decode("latin-1")
            self.p += n
        return s[:-1] if s.endswith("\0") else s


def wstr(s, force_utf16=False):
    if s == "" and not force_utf16:
        return struct.pack("<i", 0)
    if not force_utf16 and all(ord(c) < 128 for c in s):
        b = s.encode("ascii") + b"\0"
        return struct.pack("<i", len(b)) + b
    b = (s + "\0").encode("utf-16-le")
    return struct.pack("<i", -(len(b) // 2)) + b


def load(path):
    """Returns (version, [ (ns_hash, ns, [ (key_hash, key, src_hash, text) ]) ])"""
    with open(path, "rb") as f:
        data = f.read()
    r = Reader(data)
    version = 0
    strings = None
    if data[:16] == MAGIC:
        r.p = 16
        version = r.u8()
        if version >= 1:
            off = r.i64()
            save = r.p
            r.p = off
            n = r.i32()
            strings = []
            for _ in range(n):
                s = r.fstr()
                if version >= 2:
                    r.i32()
                strings.append(s)
            r.p = save
    if version >= 2:
        r.u32()  # total entry count
    out = []
    for _ in range(r.u32()):
        ns_hash = r.u32() if version >= 2 else 0
        ns = r.fstr()
        keys = []
        for _ in range(r.u32()):
            key_hash = r.u32() if version >= 2 else 0
            key = r.fstr()
            src_hash = r.u32()
            if version >= 1:
                text = strings[r.i32()]
            else:
                text = r.fstr()
            keys.append((key_hash, key, src_hash, text))
        out.append((ns_hash, ns, keys))
    return version, out


def save(path, version, namespaces):
    """Write a locres of the given version (2 or 3) keeping the supplied hashes."""
    assert version >= 2
    strings = []
    index = {}
    refs = []
    body = bytearray()
    total = sum(len(k) for _, _, k in namespaces)
    body += struct.pack("<I", total)
    body += struct.pack("<I", len(namespaces))
    for ns_hash, ns, keys in namespaces:
        body += struct.pack("<I", ns_hash) + wstr(ns)
        body += struct.pack("<I", len(keys))
        for key_hash, key, src_hash, text in keys:
            i = index.get(text)
            if i is None:
                i = index[text] = len(strings)
                strings.append(text)
                refs.append(0)
            refs[i] += 1
            body += struct.pack("<I", key_hash) + wstr(key) + struct.pack("<Ii", src_hash, i)
    head = MAGIC + bytes([version])
    off = len(head) + 8 + len(body)
    tail = bytearray(struct.pack("<i", len(strings)))
    for s, c in zip(strings, refs):
        tail += wstr(s) + struct.pack("<i", c)
    with open(path, "wb") as f:
        f.write(head + struct.pack("<q", off) + body + tail)


def to_dict(namespaces):
    return {(ns, key): (src_hash, text) for _, ns, keys in namespaces for _, key, src_hash, text in keys}

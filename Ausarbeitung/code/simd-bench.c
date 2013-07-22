void f(unsigned short *pDst, short *pSrc,
       short coeff, short intercept,
       unsigned int count) {
    int res;
    do {
        res = *pSrc++ * coeff + intercept;
        if (res & 0x80) res += 256;
        res >>= 8;
        if (res < 0) res = 0;
        if (res>0xffff) res = 0xffff;
        *pDst++ = (unsigned short) res;
    } while (--count);
}

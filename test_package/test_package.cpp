#include <iostream>
#include <tuple>

#include "h264_stream.h"

int main() {
    h264_stream_t* h = h264_new();
    h264_free(h);
    return 0;
}
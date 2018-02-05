#include <cstdlib>
#include <iostream>
#include "ltc.h"

int main()
{
	LTCEncoder* encoder = ltc_encoder_create(48000, 25., LTC_TV_625_50, 0);
	ltc_encoder_free(encoder);
	
	std::cout << "ltclib V" << LIBLTC_VERSION;
    
    return EXIT_SUCCESS;
}

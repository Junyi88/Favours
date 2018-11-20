!Use this to avoid editing multiple common blocks independently
		integer, parameter :: nElements = 94100
		integer, parameter :: nintpts = 8
		integer, parameter :: nsdv  = 89
          real*8 :: kFp, kgausscoords, kcurlFp, GND
          
      COMMON/UMPS/kFp(nElements, nintpts, 9),          
     +    kgausscoords(nElements,nintpts,3),
     +    kcurlFp(nElements, nintpts, 9),
     +    GND(8,nElements) 



      SUBROUTINE SDVINI(STATEV,COORDS,NSTATV,NCRDS,NOEL,NPT,
     1 LAYER,KSPT)
C
      INCLUDE 'ABA_PARAM.INC'
C
      INTEGER I
      REAL*8 GND
	  DIMENSION STATEV(NSTATV),COORDS(NCRDS)
      COMMON /GNDS/GND(8,98730)
	   
	  STATEV(26)=GND(NPT,NOEL)

      RETURN
      END
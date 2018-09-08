      SUBROUTINE SDVINI(STATEV,COORDS,NSTATV,NCRDS,NOEL,NPT,
     1 LAYER,KSPT)
C
      INCLUDE 'ABA_PARAM.INC'
C
      INTEGER I
      REAL*8 GND
	  DIMENSION STATEV(NSTATV),COORDS(NCRDS),GND(8)
      
	  open (200, file = 'GND.txt', status = 'old')
      do I=1,NOEL
	    read(200,*) GND
	  end do
      close(200)
	  
	  
	  STATEV(26)=GND(NPT)

      RETURN
      END
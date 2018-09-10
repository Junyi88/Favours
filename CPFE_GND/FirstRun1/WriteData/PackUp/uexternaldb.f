
      SUBROUTINE UEXTERNALDB(LOP,LRESTART,TIME,DTIME,KSTEP,KINC)
!
      INCLUDE 'ABA_PARAM.INC'
!
      DIMENSION TIME(2)
!
      INTEGER I
      REAL*8 GND
      COMMON /GNDS/GND(8,98730)  

      IF (LOP == 0 ) THEN                   
          call MutexInit( 1 )      ! initialize Mutex #1
          call MutexInit( 2 )
          call MutexInit( 3 )
		  call MutexInit( 8 )
      END IF
	  
	  IF (LOP == 0 ) THEN 
	  PRINT *, 'READ'
      call MutexLock( 8 )      ! lock Mutex #1 
	  open (200, file = 'F:\Junyi\Test1\GND.txt', status = 'old')
      do I=1,98730
	    read(200,*) GND(:,I)
	  end do
      close(200)
      call MutexUnlock( 8 )   ! unlock Mutex #1  

	  PRINT *, 'READ DONE = ', GND(2,1)	  
	  END IF
      RETURN
      END
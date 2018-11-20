
      SUBROUTINE UEXTERNALDB(LOP,LRESTART,TIME,DTIME,KSTEP,KINC)
!
      INCLUDE 'ABA_PARAM.INC'
!
      DIMENSION TIME(2)
!
       include 'mycommon.f'  
c       write(6,*) "MWTF---------------------------"
      IF (LOP == 0 ) THEN                   
          call MutexInit( 1 )      ! initialize Mutex #1
          call MutexInit( 2 )
          call MutexInit( 3 )
          call MutexInit( 4 )
          call MutexInit( 5 )
          call MutexInit( 6 )
          
          call MutexInit( 7 )
c       write(6,*) "MUTEXINIT---------------------------"

c       get Reader
      call MutexLock( 7 )
      open (200, file = 'F:\Junyi\GNDInitial\GND.txt', status = 'old')
      do I=1,nElements
        read(200,*) GND(1:8,I)
      end do
      close(200)
      
      END IF
      PRINT *, 'READ DONE = ', GND(2,1)	  
      call MutexUnLock( 7 )    


      RETURN
      END
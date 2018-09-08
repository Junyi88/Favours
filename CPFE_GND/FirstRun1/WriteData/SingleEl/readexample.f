        program FWORDX
        IMPLICIT REAL*8 (A-H,O-Z)
        REAL*8 X1,X2,X3,X4,XX
        INTEGER I
       DIMENSION X1(4),X2(4),X3(4),X4(4), XX(4,4)

       open (2, file = 'moron.txt', status = 'old')
       do i = 1,4
        read(2,*) x1(i), x2(i), x3(I), x4(I)
       end do

       do i=1,4
        print *, I, x1(I), X2(I), X3(I), X4(I)
       end do
       close(2)

       open (2, file = 'moron.txt', status = 'old')
       do i = 1,4
        read(2,*) XX(I,:)
       end do
       print *, "MORON"
       do i=1,4
        print *, I, XX(I,:)
       end do
       close(2)

      RETURN
      END
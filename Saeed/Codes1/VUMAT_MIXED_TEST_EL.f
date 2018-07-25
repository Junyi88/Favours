*USER SUBROUTINE
      SUBROUTINE VUMAT(
     1 NBLOCK, NDIR, NSHR, NSTATEV, NFIELDV, NPROPS, LANNEAL,
     2 STEPTIME, TOTALTIME, DT, CMNAME, COORDMP, CHARLENGTH,
     3 PROPS, DENSITY, STRAININC, RELSPININC,
     4 TEMPOLD, STRETCHOLD, DEFGRADOLD, FIELDOLD,
     5 STRESSOLD, STATEOLD, ENERINTERNOLD, ENERINELASOLD,
     6 TEMPNEW, STRETCHNEW, DEFGRADNEW, FIELDNEW,
     7 STRESSNEW, STATENEW, ENERINTERNNEW, ENERINELASNEW)
C
        INCLUDE 'VABA_PARAM.INC'
C
C
C THE STATE VARIABLES ARE STORED AS:
C         STATE(*,1) = RELATIVE DENSITY
C         STATE (*,2) = GRAIN GROWTH
C
C
      DIMENSION PROPS(NPROPS), DENSITY(NBLOCK),
     1 COORDMP(NBLOCK,*),
     2 CHARLENGTH(NBLOCK), STRAININC(NBLOCK,NDIR+NSHR),
     3 RELSPININC(NBLOCK), TEMPOLD(NBLOCK),
     4 STRETCHOLD(NBLOCK,NDIR+NSHR), DEFGRADOLD(NBLOCK,NDIR+NSHR),
     5 FIELDOLD(*), STRESSOLD(NBLOCK,NDIR+NSHR),
     6 STATEOLD(NBLOCK,NSTATEV), ENERINTERNOLD(NBLOCK),
     7 ENERINELASOLD(NBLOCK), TEMPNEW(*),
     8 STRETCHNEW(NBLOCK,NDIR+NSHR),DEFGRADNEW(NBLOCK,NDIR+NSHR+NSHR),
     9 FIELDNEW(*), STRESSNEW(NBLOCK,NDIR+NSHR),
     1 STATENEW(NBLOCK,NSTATEV), ENERINTERNNEW(NBLOCK),
     2 ENERINELASNEW(NBLOCK)
C
        CHARACTER*80 CMNAME
C
	  PARAMETER (M=3,N=3,ID=3,ZERO=0.0,ONE=1.0,TWO=2.0,THREE=3.0,
     1     THIRD=ONE/THREE,HALF=.5,TWOTHIRDS=TWO/THREE,THREEHALFS=1.5,
     2     COEFN=10.0, EPSDOTZ=5.0, SIGMAZERO=500.0)
        
C
C        
      REAL*8 TERM4,ST2,KUHN,DCD1,DCD2,DCD,DIVIASR
        
      DIMENSION DFGI(M,N),DFGR(M,N),XIDEN(M,N),DFGRD0(M,N),DFGRD1(M,N),
     + VEG(M,N),TVEG(M,N),DFRT(M,N),STRET0(M,N),STRET1(M,N),
     + STR(M,N),STRR(M,N),DSTR(M,N),STRETI0(M,N),STRETI1(M,N),
     + SPINW(M,N),WS(M,N),SW(M,N),XROT0(M,N),XROT1(M,N),
     + XRDOT(M,N),XROT0TR(M,N),XOMEGA(M,N),DCD(M,N),DEL(M,N),
     + KUHN(M,N),TERM4(M,N),ST2(M,N),DCD1(M,N),DCD2(M,N),DIVIASR(M,N),
     + TSTR(M,N)
 
C--------------------------------------------------------------------



C—---SECTION I
C
C
C OBTAIN THE MATERIAL PROPERTIES E AND NUE 
C


        QE=8.018E3
        E0=4.748E4 
        Rg=8.314
        
        XNUE=0.3

        TEMPR=Rg*(TEMPNEW(1) + 273.15)

        E=E0*EXP(QE/TEMPR)   !E is around 95,000 MPa at 1150 C

C DBG

C         write(*,*) "================================================="

C
        EBULK3 = E/(ONE-TWO*XNUE)
        EG = E/(ONE+XNUE)
        ELAM = (EBULK3-EG)/THREE
       
C        SHM = E/(2.0*(ONE+XNUE))
            
C
C--------------------------------------------------------------------
C
C START THE MATERIAL CONSTITUTIVE EQUATIONS AT EACH INTEGRATION
C POINT
C
      DO 100 KM = 1,NBLOCK
C
C--------------------------------------------------------------------
C
C----SECTION II
C
C
C WRITE STRESSES FROM PREVIOUS TIME STEP IN TO ARRAY STR
C
        write(*,*) " ______________________________________________" 
		
        DO K=1,3
        STR(K,K) = STRESSOLD(KM,K)
        END DO
        STR(1,2) = STRESSOLD(KM,4)
        STR(2,1) = STRESSOLD(KM,4)
C        IF(NTENS.GT.4)THEN
        STR(2,3) = STRESSOLD(KM,5)
        STR(3,2) = STRESSOLD(KM,5)
        STR(1,3) = STRESSOLD(KM,6)
        STR(3,1) = STRESSOLD(KM,6)
C        END IF


C
C DEFINE IDENTITY MATRIX
C
        DO 50 I=1,M
        DO 50 J=1,N
        IF(I .EQ. J) THEN
        XIDEN(I,J)=1.0D0
        ELSE
        XIDEN(I,J)=0.0D0
        END IF
50      CONTINUE
C
C
C CALCULATE DEVIATORIC STRESS (DSTR) AND MEAN STRESS (1/3)*TR(SIGMA)
C 
         write(*,*) "CP1 STR = " ,  STR(1,1) , STR(1,2) , STR(1,3) 
         write(*,*) "CP1 STR = " ,  STR(2,1) , STR(2,2) , STR(2,3) 
         write(*,*) "CP1 STR = " ,  STR(3,1) , STR(3,2) , STR(3,3) 
         write(*,*) "    " 
		 
         CALL KDEVIA(STR,XIDEN,DSTR,MSTR)
		 
         write(*,*) "CP2 DSTR = " ,  DSTR(1,1) , DSTR(1,2) , DSTR(1,3) 
         write(*,*) "CP2 DSTR = " ,  DSTR(2,1) , DSTR(2,2) , DSTR(2,3) 
         write(*,*) "CP2 DSTR = " ,  DSTR(3,1) , DSTR(3,2) , DSTR(3,3) 
         write(*,*) "    " 
		 
         write(*,*) "CP2 STR = " ,  STR(1,1) , STR(1,2) , STR(1,3) 
         write(*,*) "CP2 STR = " ,  STR(2,1) , STR(2,2) , STR(2,3) 
         write(*,*) "CP2 STR = " ,  STR(3,1) , STR(3,2) , STR(3,3) 
         write(*,*) "    " 
		 
         write(*,*) " MSTR = " ,  DMSTR
         write(*,*) "    " 
		 
C
C CALCULATE EFFECTIVE STRESS AS SQRT((3/2)*DSTR:DSTR)
C
        CALL KEFFP(DSTR,EFFSTR)

         write(*,*) "CP3 EFFSTR = " ,  EFFSTR
         write(*,*) "CP3 DSTR = " ,  DSTR(1,1) , DSTR(1,2) , DSTR(1,3) 
         write(*,*) "CP3 DSTR = " ,  DSTR(2,1) , DSTR(2,2) , DSTR(2,3) 
         write(*,*) "CP3 DSTR = " ,  DSTR(3,1) , DSTR(3,2) , DSTR(3,3) 
         write(*,*) "    " 
C
C--------------------------------------------------------------------
C
C STORE THE DEFROMATION GRADIENT AND THE STRETCH TENSORS
C
C WRITE THE DEFORMATION GRADIENT TENSOR AT PREVIOUS TIME STEP
C INTO DFGRAD0
C
      DO K=1,3
      DFGRD0(K,K) = DEFGRADOLD(KM,K)
      END DO
      DFGRD0(1,2) = DEFGRADOLD(KM,4)
      DFGRD0(2,1) = DEFGRADOLD(KM,7)
      DFGRD0(2,3) = DEFGRADOLD(KM,5)
      DFGRD0(3,2) = DEFGRADOLD(KM,8)
      DFGRD0(1,3) = DEFGRADOLD(KM,6)
      DFGRD0(3,1) = DEFGRADOLD(KM,9)
C
C WRITE THE DEFORMATION GRADIENT TENSOR AT NEXT TIME STEP
C INTO DFGRAD1
C
      DO K=1,3
      DFGRD1(K,K) = DEFGRADNEW(KM,K)
      END DO
      DFGRD1(1,2) = DEFGRADNEW(KM,4)
      DFGRD1(2,1) = DEFGRADNEW(KM,7)
      DFGRD1(2,3) = DEFGRADNEW(KM,5)
      DFGRD1(3,2) = DEFGRADNEW(KM,8)
      DFGRD1(1,3) = DEFGRADNEW(KM,6)
      DFGRD1(3,1) = DEFGRADNEW(KM,9)
C
C
C WRITE THE STRETCH TENSOR “U” DEFINED BY F=R*U AT PREVIOUS TIME
C STEP INTO STRET0
C
      DO K=1,3
      STRET0(K,K) = STRETCHOLD(KM,K)
      END DO
      STRET0(1,2) = STRETCHOLD(KM,4)
      STRET0(2,1) = STRETCHOLD(KM,4)
      STRET0(2,3) = STRETCHOLD(KM,5)
      STRET0(3,2) = STRETCHOLD(KM,5)
      STRET0(1,3) = STRETCHOLD(KM,6)
      STRET0(3,1) = STRETCHOLD(KM,6)
C
C WRITE THE STRETCH TENSOR “U” DEFINED BY F=R*U AT NEXT TIME STEP
C INTO STRET1
C
      DO K=1,3
      STRET1(K,K) = STRETCHNEW(KM,K)
      END DO
      STRET1(1,2) = STRETCHNEW(KM,4)
      STRET1(2,1) = STRETCHNEW(KM,4)
      STRET1(2,3) = STRETCHNEW(KM,5)
      STRET1(3,2) = STRETCHNEW(KM,5)
      STRET1(1,3) = STRETCHNEW(KM,6)
      STRET1(3,1) = STRETCHNEW(KM,6)
C
C
C--------------------------------------------------------------------
C
C-----SECTION III
C
C STEPS TO CALCULATE THE OMAGA TENSOR OMEGA = R_DOT*R_TRANSPOSE
C
C
C TO DETERMINE THE “R” FROM THE POLAR DECOMPOSITION OF F=RU
C
C FIRST DETERMINE THE INVERSE OF STRETCH TENSOR “U” AT BOTH TIME
C INSTANCES
C
         write(*,*) "CP4" 
         write(*,*) "STRET0 = ", STRET0(1,1), STRET0(1,2), STRET0(1,3) 
         write(*,*) "STRET0 = ", STRET0(2,1), STRET0(2,2), STRET0(2,3) 
         write(*,*) "STRET0 = ", STRET0(3,1), STRET0(3,2), STRET0(3,3) 
         write(*,*) "    " 

         CALL KINVER(STRET0,STRETI0)
		
         write(*,*) "CP5" 
         write(*,*) "STRETI0= ", STRETI0(1,1),STRETI0(1,2),STRETI0(1,3) 
         write(*,*) "STRETI0= ", STRETI0(2,1),STRETI0(2,2),STRETI0(2,3) 
         write(*,*) "STRETI0= ", STRETI0(3,1),STRETI0(3,2),STRETI0(3,3) 
         write(*,*) "    " 		
         write(*,*) "STRET0= ", STRET0(1,1), STRET0(1,2), STRET0(1,3) 
         write(*,*) "STRET0= ", STRET0(2,1), STRET0(2,2), STRET0(2,3) 
         write(*,*) "STRET0= ", STRET0(3,1), STRET0(3,2), STRET0(3,3) 
         write(*,*) "    " 	
         write(*,*) "STRET1= ", STRET1(1,1), STRET1(1,2), STRET1(1,3) 
         write(*,*) "STRET1= ", STRET1(2,1), STRET1(2,2), STRET1(2,3) 
         write(*,*) "STRET1= ", STRET1(3,1), STRET1(3,2), STRET1(3,3) 	
         write(*,*) "    " 	
		 
         CALL KINVER(STRET1,STRETI1)
		
         write(*,*) "CP6" 
         write(*,*) "STRETI1= ", STRETI1(1,1),STRETI1(1,2),STRETI1(1,3) 
         write(*,*) "STRETI1= ", STRETI1(2,1),STRETI1(2,2),STRETI1(2,3) 
         write(*,*) "STRETI1= ", STRETI1(3,1),STRETI1(3,2),STRETI1(3,3) 
         write(*,*) "    " 		
         write(*,*) "STRET1= ", STRET1(1,1), STRET1(1,2), STRET1(1,3) 
         write(*,*) "STRET1= ", STRET1(2,1), STRET1(2,2), STRET1(2,3) 
         write(*,*) "STRET1= ", STRET1(3,1), STRET1(3,2), STRET1(3,3) 
         write(*,*) "    " 	
        
   
C
C CALCULATE “R” AT BOTH THE TIME INSTANCES AS XROT0 AND XROT1
C
         write(*,*) "CP7" 
         write(*,*) "DFGRD0= ", DFGRD0(1,1),DFGRD0(1,2),DFGRD0(1,3) 
         write(*,*) "DFGRD0= ", DFGRD0(2,1),DFGRD0(2,2),DFGRD0(2,3) 
         write(*,*) "DFGRD0= ", DFGRD0(3,1),DFGRD0(3,2),DFGRD0(3,3) 
         write(*,*) "    " 		

        CALL KMLT(DFGRD0,STRETI0,XROT0)
		
         write(*,*) "CP7" 
         write(*,*) "XROT0= ", XROT0(1,1), XROT0(1,2), XROT0(1,3) 
         write(*,*) "XROT0= ", XROT0(2,1), XROT0(2,2), XROT0(2,3) 
         write(*,*) "XROT0= ", XROT0(3,1), XROT0(3,2), XROT0(3,3) 
         write(*,*) "    " 		
         write(*,*) "DFGRD1= ", DFGRD1(1,1),DFGRD1(1,2),DFGRD1(1,3) 
         write(*,*) "DFGRD1= ", DFGRD1(2,1),DFGRD1(2,2),DFGRD1(2,3) 
         write(*,*) "DFGRD1= ", DFGRD1(3,1),DFGRD1(3,2),DFGRD1(3,3) 
         write(*,*) "    " 				 
		 
        CALL KMLT(DFGRD1,STRETI1,XROT1)

         write(*,*) "CP8" 
         write(*,*) "XROT1= ", XROT1(1,1), XROT1(1,2), XROT1(1,3) 
         write(*,*) "XROT1= ", XROT1(2,1), XROT1(2,2), XROT1(2,3) 
         write(*,*) "XROT1= ", XROT1(3,1), XROT1(3,2), XROT1(3,3) 
         write(*,*) "    " 		
C
C
C DETERMINE RDOT
C
      IF(DT.GT.0.) THEN
      DO 99 I=1,M
      DO 99 J=1,N
      XRDOT(I,J)=(XROT1(I,J)-XROT0(I,J))/DT
99    CONTINUE
      END IF

         write(*,*) "CP9" 
         write(*,*) "DT= ", DT
         write(*,*) "XRDOT= ", XRDOT(1,1), XRDOT(1,2), XRDOT(1,3) 
         write(*,*) "XRDOT= ", XRDOT(2,1), XRDOT(2,2), XRDOT(2,3) 
         write(*,*) "XRDOT= ", XRDOT(3,1), XRDOT(3,2), XRDOT(3,3) 
         write(*,*) "    " 
C
C
C CALCULATE R_TRANSPOSE
C
        CALL KTRANS(XROT0,XROT0TR)
C
C
C CALCULATE OMEGA = R_DOT*R_TRANSPOSE
C
        CALL KMLT(XRDOT,XROT0TR,XOMEGA)
        
C
C
C--------------------------------------------------------------------
C
C----SECTION IV
C
C
C STEPS TO DETERMINE THE SYMMETRIC PART OF VELOCITY GRADIENT
C
C
C DETERMINE DEFORMATION GRADIENT RATE F_DOT
C
      IF(DT.GT.0.) THEN
      DO 110 I=1,M
      DO 110 J=1,N
      DFGR(I,J)=(DFGRD1(I,J)-DFGRD0(I,J))/DT
110   CONTINUE
      END IF
C
C TO DETERMINE VELOCITY GRADIENT
C
C FIRST DETERMINE THE INVERSE OF DEFORMATION GRADIENT
C
        CALL KINVER(DFGRD0,DFGI)
C
C THEN CALCULATE L=FDOT*FINV
C
        CALL KMLT(DFGR,DFGI,VEG)
C
C TO DETERMINE RATE OF DEFORMATION FROM VELOCITY GRADIENT
C
C FIRST DETERMINE THE TRANSPOSE OF L
C
        CALL KTRANS(VEG,TVEG)
C
C
        DO 120 I=1,M
        DO 120 J=1,N
        DFRT(I,J)=(ONE/TWO)*(VEG(I,J)+TVEG(I,J))
120   CONTINUE

    
      write(*,*) " DFRT1 = " ,  DFRT(1,1) , DFRT(1,2) , DFRT(1,3) 
      write(*,*) " DFRT2 = " ,  DFRT(2,1) , DFRT(2,2) , DFRT(2,3)
      write(*,*) " DFRT3 = " ,  DFRT(3,1) , DFRT(3,2) , DFRT(3,3)
      write(*,*) "    " 
      
      
!C     CALCULATE TOTAL STRAIN 'RATE' TENSOR FROM STRAIN INCREMENT
!       DO 920 I=1,M
!       DO 920 J=1,N
!       TSTR(I,J)=0.0
!       
!       IF (DT.GT.0.0) TSTR(I,J)=DBLE(STRAININC(I,J))/DBLE(DT)
!       
! 920   CONTINUE
      
  
      
C
C
C--------------------------------MIXED FUNCTION---------------------------------------------
C
!!C-----SECTION V
!!
!!      DCRD=STATEOLD(KM,1)
!!      
!!      DEN0=0.7  
!!      
!!C -------------------STRAIN RATE OF KUHN AND MCMEEKING D<0.9-----------------------------
!!
!!C STORE THE CURRENT RELATIVE DENSITY IN THE VARIABLE DCRD
!!
!!      
!!      TERM1=EPSDOTZ*(27.0*3.14/(16.0*SQRT(3.0)))*SQRT((DCRD-DEN0)/(1.0
!!     +      -DEN0))
!!     
!!     
!!      !IF(DCRD-DEN0.EQ.0.0) THEN
!!      !TERM2=0.0
!!      !ELSE
!!      TERM2=((1.0-DEN0)/((3.0*DCRD**2.0)*(DCRD-DEN0)))**COEFN 
!!      !END IF
!!      
!!      
!!      TERM3=(((ABS(MSTR)/SIGMAZERO)**((COEFN+1.0)/COEFN))
!!     +      + (2.0*EFFSTR/(3.0*SIGMAZERO))**((COEFN+1.0)/COEFN))
!!     +       **(COEFN-1.0)
!!     
!!      
!!      
!!        DO I = 1,3
!!        DO J = 1,3
!!        IF(EFFSTR.EQ.0.0 .OR. MSTR.EQ.0.0) THEN
!!        TERM4(I,J)=0.0     
!!        ELSE 
!!            
!!        IF(I.EQ.J) THEN 
!!     
!!        TERM4(I,J)=((ABS(MSTR)/SIGMAZERO)**(1.0/COEFN))*
!!     +             (ABS(1.0)*(MSTR/ABS(MSTR)))*(1.0/3.0) + 
!!     +  ((2.0*EFFSTR/(3.0*SIGMAZERO))**(1.0/COEFN))*(DSTR(I,J)/EFFSTR)
!!     
!!        ELSE 
!!            
!!        TERM4(I,J)= ((2.0*EFFSTR/(3.0*SIGMAZERO))**(1.0/COEFN))
!!     +            *(DSTR(I,J)/EFFSTR)
!!      
!!
!!        END IF
!!        END IF
!!        END DO
!!        END DO
!!     
!!
!!      DO I = 1,3
!!      DO J = 1,3
!!             
!!      KUHN(I,J) = TERM1*TERM2*TERM3*TERM4(I,J)
!!      
!!      END DO
!!      END DO
!!      
!!      
!!         write(*,*) "TERM1 = " , TERM1
!!         write(*,*) "TERM2 = " , TERM2
!!         write(*,*) "TERM3 = " , TERM3
!!         write(*,*) "TERM4(1,1) = " , TERM4(1,1)
!!         write(*,*) "KUHN(1,1) = " , KUHN(1,1)
!!        
!!        
!!        
!!      
!!  
!!C----------------------STRAIN RATE FOR STAGE 2, D>0.9----------------------------------
!!
!!C CALCULATE THE COEFFICIENTS a AND b GIVEN BY PONTE MODEL------------------------------        
!!        
!!      DCA = (ONE + (TWO/THREE)*(ONE-DCRD))/(DCRD**(2.0*COEFN/
!!     +      (COEFN+1.0)))
!!      
!!      DCB = 2.25*(ONE-DCRD)*DCRD**((-1.0)*(TWO*COEFN/(COEFN+1.0)))
!!
!!C
!!C CALCULATE THE EFFECTIVE STRESS DEFINED BY PONTE MODEL
!!C
!!        PJ2 = DCA*EFFSTR**TWO + DCB*MSTR**TWO
!!        PJ = SQRT(PJ2)
!!    
!!C
!!C DEFINE A GIVEN BY EPSILON_ZERO_DOT/SIGMA_ZERO^N
!!C
!!        CONSTA = EPSDOTZ/(SIGMAZERO**COEFN)
!!
!!C
!!C CALCULATE THE D_P (PLASTIC STRAINE RATE) GIVEN BY THE PONTE MODEL
!!C
!!        DO I = 1,3
!!        DO J = 1,3
!!        IF(I .EQ. J) THEN
!!        ST2(I,J) = CONSTA*(PJ**(COEFN-ONE))
!!     +             *(THREE*DCA*DSTR(I,J)/TWO + DCB*MSTR/THREE)
!!        ELSE
!!        ST2(I,J) = CONSTA*(PJ**(COEFN-ONE))*(THREE*DCA*DSTR(I,J)/TWO)
!!        
!!        END IF
!!        END DO
!!        END DO
!!
!!C
!!C---------------------------INTERPOLATION RULE------------------------------------
!!      
!!      DEN1=0.8 
!!      DEN2=0.9
!!C
!!      DO I = 1,3
!!      DO J = 1,3
!!      DCD1(I,J)=((DEN2-DCRD)/(DEN2-DEN1))*KUHN(I,J)
!!      DCD2(I,J)=((DCRD-DEN1)/(DEN2-DEN1))*ST2(I,J)
!!      DCD(I,J) = DCD1(I,J) + DCD2(I,J)
!!      END DO
!!      END DO
!!  
!!       !STATENEW(KM,3)=DCD1(2,2)
!!       !STATENEW(KM,4)=DCD2(2,2)
!!       !STATENEW(KM,5)=DCD(2,2)
!!       !STATENEW(KM,6)=TERM4(2,2)
!!       !STATENEW(KM,7)=KUHN(2,2)
!!
!!C
!!C      
!!C CALCULATE THE DILATATION = TRACE (D_P) AS DCTRVAL------------
!!C
!!C
!!        CALL KTRACE(DCD,DCTRVAL)        
!!        
!!
!!C-----------------------------GRAIN GROWTH-------------------------------------       
!!      
!!      GRAINGROWTH=STATEOLD(KM,2)
!!       K1=1.5
!!       PARAD=35.0
!!       GRAINSIZE=2.0*PARAD
!!       
!!      STRCONC1=(1.0-DEN0)/((DCRD**2.0)*(DCRD-DEN0))
!!      STRCONC2=1.0/DCRD
!!        
!!      STRCONC11=((DEN2-DCRD)/(DEN2-DEN1))*STRCONC1
!!      STRCONC22=((DCRD-DEN1)/(DEN2-DEN1))*STRCONC2
!!      STRCONC=STRCONC11 + STRCONC22
!!        
!!      GGR1=K1*GRAINSIZE/STRCONC
!!     
!!      
!!        DO I = 1,3
!!        DO J = 1,3
!!        IF(I .NE. J) THEN
!!
!!        DIVIASR(I,J) = DCD(I,J)
!!        
!!        END IF
!!        END DO
!!        END DO
!!      
!!       GGR=GGR1*SQRT((DIVIASR(I,J)*DIVIASR(I,J))+(((DCTRVAL)**2.0)/3.0))
!!       
            
C---------------------------------------------------------------------------------------

C
C-----SECTION VI
C
C
C CALCULATE THE D_E, THE OBJECTIVE STRESS RATE AND STRESS RATE
C
C
C CALCULATE D_E = D – D_E
C
       
         DO 150 I = 1,3
         DO 150 J = 1,3
              
         DEL(I,J) = DFRT(I,J) 
                          
150      CONTINUE
       
      !write(*,*) " DEL1 = " ,  DEL(1,1) , DEL(1,2) , DEL(1,3) 
      !write(*,*) " DEL2 = " ,  DEL(2,1) , DEL(2,2) , DEL(2,3)
      !write(*,*) " DEL3 = " ,  DEL(3,1) , DEL(3,2) , DEL(3,3)
          

!        IF (STEPTIME.EQ.0.0) THEN
!        
!        DO 150 I = 1,3
!        DO 150 J = 1,3
!           DEL(I,J) = DFRT(I,J) 
!150   CONTINUE
!      
!      ELSE
!   
!        DO 850 I = 1,3
!        DO 850 J = 1,3
!        DEL(I,J) = DFRT(I,J) - DCD(I,J)
!850     CONTINUE
!      END IF


C
C CALCULATE THE TRACE OF D_E
C
        CALL KTRACE(DEL,TRVAL)
        
C
C DETERMINE GREEN-NAGHDI STRESS RATE
C
      DO 160 I=1,M
      DO 160 J=1,N
      STRR(I,J)= EG*DEL(I,J) + ELAM*TRVAL*XIDEN(I,J)
160   CONTINUE
C
C
C DETERMINE STRESS RATE WRT UNDEFORMED CONFIGURATION
C
        CALL KMLT(XOMEGA,STR,WS)
        CALL KMLT(STR,XOMEGA,SW)
C
C
      DO 231 I=1,M
      DO 231 J=1,N
      STRR(I,J)=STRR(I,J)+WS(I,J)-SW(I,J)
C
C .... AND INTEGRATE
C
      
      STR(I,J) = STR(I,J) + STRR(I,J)*DT
231   CONTINUE
      
      
      
      !write(*,*) " STR1 = " ,  STR(1,1) , STR(1,2) , STR(1,3) 
      !write(*,*) " STR2 = " ,  STR(2,1) , STR(2,2) , STR(2,3)
      !write(*,*) " STR3 = " ,  STR(3,1) , STR(3,2) , STR(3,3)
      
      
  
C
C
C--------------------------------------------------------------------
C
C-----SECTION VII
C
C
C UPDATE THE STRESS AND THE RELATIVE DENSITY
C
C
C WRITE UPDATED STRESSES IN TO ABAQUS ARRAY STRESSNEW
C
      DO I=1,3
      STRESSNEW(KM,I)=STR(I,I)
      END DO
      STRESSNEW(KM,4)=STR(1,2)
      STRESSNEW(KM,5)=STR(1,3)
      STRESSNEW(KM,6)=STR(2,3)
C
C
C UPDATE THE RELATIVE DENSITY
C
!      IF (STEPTIME.EQ.0.0) THEN
!          STATENEW(KM,1)=STATEOLD(KM,1)
!          STATENEW(KM,2)=STATEOLD(KM,2)
!      ELSE
!          
!      DCRDDOT = -1.0*DCRD*DCTRVAL
!      DCRD = DCRD + DCRDDOT*DT
!      STATENEW(KM,1)=DCRD
!      IF(DCRD.GT.1.0) THEN
!      DCRD=1.0
!      END IF
!
!C UPDATE THE GRAINGROWTH
!C
!      GRAINGROWTH = GRAINGROWTH + GGR*DT
!      STATENEW(KM,2)=GRAINGROWTH
!      END IF
      
C
100   CONTINUE
C
      RETURN
      END
C
C--------------------------------------------------------------------
C
***********************************************
** UTILITY SUBROUTINES *
***********************************************
**************************************
** INVERSE MATRIX *
**************************************
**
*USER SUBROUTINE
        SUBROUTINE KINVER(DF,A)
C
        INCLUDE 'VABA_PARAM.INC'
C
        PARAMETER (M=3,N=3)
        DIMENSION DF(M,N),A(M,N)
C
        DO 5 I=1,M
        DO 5 J=1,N
        A(I,J)=DF(I,J)
5       CONTINUE
        DO 10 K=1,M
        P=A(K,K)
        A(K,K)=1.
        DO 20 J=1,N
        A(K,J)=A(K,J)/P
20      CONTINUE
        DO 10 I=1,M
        IF(I .EQ. K) GO TO 10
        P=A(I,K)
        A(I,K)=0.
        DO 30 J=1,N
        A(I,J)=A(I,J)-A(K,J)*P
30      CONTINUE
10      CONTINUE
        RETURN
        END
**
**
**************************************
** MULTIPLY MATRIX *
**************************************
**
*USER SUBROUTINE
        SUBROUTINE KMLT(DM1,DM2,DM)
C
        INCLUDE 'VABA_PARAM.INC'
C
        PARAMETER (M=3,N=3)
        DIMENSION DM1(M,N),DM2(M,N),DM(M,N)
C
        DO 10 I=1,M
        DO 10 J=1,N
        X=0.0
        DO 20 K=1,M
        X=X+DM1(I,K)*DM2(K,J)
20      CONTINUE
        DM(I,J)=X
10      CONTINUE
        RETURN
        END
**
**
***************************************
** EFFECTIVE STRESS *
***************************************
**
*USER SUBROUTINE
        SUBROUTINE KEFFP(EFF1,VAL1)
C
        INCLUDE 'VABA_PARAM.INC'
C
        PARAMETER (M=3,N=3)
        DIMENSION EFF1(M,N)
C
        X=0.0
        DO 10 I=1,M
        DO 10 J=1,N
        X=X+EFF1(I,J)*EFF1(I,J)
10      CONTINUE
        IF(X .LE. 0.0) GO TO 20
        VAL1=SQRT((3.0/2.0)*X)
20      RETURN
        END
**
**
**
***************************************
** TRACE OF MATRIX CALCULATION *
***************************************
**
*USER SUBROUTINE
        SUBROUTINE KTRACE(DE,TVAL)
C
        INCLUDE 'VABA_PARAM.INC'
C
        PARAMETER (M=3,N=3)
        DIMENSION DE(M,N)
C
        X=0.0
        DO 10 I=1,M
        DO 10 J=1,N
        IF(I .EQ. J) THEN
        X=X+DE(I,J)
        ELSE
        END IF
10      CONTINUE
        TVAL=X
        RETURN
        END
**
**
*****************************************************
** DEVIATORIC AND MEAN STRESS CALCULATION *
*****************************************************
*USER SUBROUTINE
      SUBROUTINE KDEVIA(STRSS,XIDENTY,DEVITO,MSTR)
C      
      INCLUDE 'VABA_PARAM.INC'
C
      PARAMETER (M=3,N=3)
      DIMENSION STRSS(M,N),XIDENTY(M,N),DEVITO(M,N)
C
      X=0.0
      DO 10 I=1,M
      DO 10 J=1,N
      IF(I .EQ. J) THEN
      X=X+STRSS(I,J)
      ELSE
      END IF
10    CONTINUE
      
      MSTR=X/3.0
C
      DO 20 I=1,M
      DO 20 J=1,N
      IF(I .EQ. J) THEN
        DEVITO(I,J)=STRSS(I,J)-((1./3.)*X*XIDENTY(I,J))
      ELSE
        DEVITO(I,J)=STRSS(I,J)
      END IF
20    CONTINUE
      RETURN
      END
**
**
******************************************************
** TRANSPOSE OF MATRIX *
******************************************************
**
*USER SUBROUTINE
        SUBROUTINE KTRANS(ORIGN,TRAN)
C
        INCLUDE 'VABA_PARAM.INC'
C
        PARAMETER (M=3,N=3)
        DIMENSION ORIGN(M,N),TRAN(M,N)
C
        DO 10 I=1,M
        DO 10 J=1,N
        TRAN(J,I)=ORIGN(I,J)
10      CONTINUE
        RETURN
        END
**
**
**
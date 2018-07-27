function [Values]=GetYoungsPoisson(K)


C=inv(K);

Values.YMx=1./C(1,1);
Values.YMy=1./C(2,2);
Values.YMz=1./C(3,3);

Values.nuxy=C(2,1).*(-Values.YMx);
Values.nuyx=C(1,2).*(-Values.YMy);

Values.nuxz=C(3,1).*(-Values.YMx);
Values.nuzx=C(1,3).*(-Values.YMz);

Values.nuzy=C(2,3).*(-Values.YMz);
Values.nuyz=C(3,2).*(-Values.YMy);

Values.EL=K(3,3)-2.*(K(1,3).^2)./(K(1,1)+K(1,2));
Values.ET=(K(1,1)-K(1,2)).*...
    (K(1,1).*K(3,3)+K(1,2).*K(3,3)-2.*K(1,3).*K(1,3))./...
    (K(1,1)*K(3,3)-K(1,3).^2);
Values.NuLT=K(1,3)./(K(1,1)+K(1,2));

end
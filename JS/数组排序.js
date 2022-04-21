a = [3,1,2,5,7,4];
x = a[0];
y = a[0];

for(i = 1;i<a.length;i++){
    if(a[i] > x){
        x = a[i]
    }
}

for(i = 1;i < a.length;i++){
    if(a[i] < x)
        y = a[i]
}
console(x,y);


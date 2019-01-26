var arr=["apple",["apple","banana","strawberry","orange","apple"],["apple"],"apple"];
//console.log(arr)
var item="apple";
var count = 0;
for(var i=0;i<arr.length;i++)
{
    if(arr[i]==item)
        count++;
    else if(arr[i].length > 0)
    {
        console.log("its an array having len"+arr[i].length);
        for(var j=0;j<arr[i].length;j++)
        {
           // console.log(arr[i][j]);
            if(arr[i][j]==item)
            {
                count++;
            }
        }
    }
}


console.log("count is "+count);
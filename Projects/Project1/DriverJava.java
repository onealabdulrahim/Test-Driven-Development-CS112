public class DriverJava{

static String[] tests = {
/*YOUR TESTS GO BELOW THIS LINE*/
"triangleType 5 5 5",
"equilateral",
"triangleType 5 5 3",
"isosceles",
"triangleType 4 5 5",
"isosceles",
"triangleType 5 4 5",
"isosceles",
"triangleType 0 0 0",
"Not a valid triangle!",
"triangleType 3 4 5",
"scalene",
"triangleType 4 5 3",
"scalene",
"triangleType 4 3 5",
"scalene",
"triangleType 5 3 4",
"scalene",
"triangleType 5 4 3",
"scalene",
"triangleType 1 2 3",
"Not a valid triangle!",
"triangleType 3 2 1",
"Not a valid triangle!",
"triangleType 3 1 2",
"Not a valid triangle!",
"triangleType 1 3 2",
"Not a valid triangle!",
"triangleType 2 3 1",
"Not a valid triangle!",
"triangleType 2 1 3",
"Not a valid triangle!",
/*DO NOT CHANGE ANYTHING BELOW THIS LINE*/
" "};
public static String getTest(int i){
return tests[i];
}
	
public static String getResult(int i){
return tests[i+1];
}
}
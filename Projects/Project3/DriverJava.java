public class DriverJava{

static String[] tests = {"create 3 4 two",
"[1, 2, 3, 5, 7, 10, 11, 12]",
"create 3 3 one",
"[3, 6, 9]",
"create 3 3 two",
"[1, 2, 3, 5, 7, 8, 9]",
"create 3 4 two",
"[1, 2, 3, 5, 7, 10, 11, 12]",
"create 4 3 two",
"[1, 2, 3, 4, 6, 7, 9, 10, 11, 12]",
"create 4 4 two",
"[1, 2, 3, 4, 6, 7, 9, 13, 14, 15, 16]",
"create 5 5 two",
"[1, 2, 3, 4, 5, 10, 12, 13, 14, 16, 21, 22, 23, 24, 25]",
"create 10 10 two",
"[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 42, 43, 44, 45, 46, 47, 48, 49, 51, 61, 71, 81, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]",
" "};
public static String getTest(int i){
return tests[i];
}
	
public static String getResult(int i){
return tests[i+1];
}
}
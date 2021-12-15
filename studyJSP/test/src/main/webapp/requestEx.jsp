<%@page import="java.util.Arrays"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

	<%-- 선언문으로 form 태그에서 넘어올 변수들을 선언하고 
		 스크립트릿으로 넘어온 데이터를 받아 표현식으로 브라우저에 출력하기 --%>
		 
	
	<%!
		String name, age, number, FnumID, BnumID, area;
		String[] habit;
	%>


	<%
		request.setCharacterEncoding("UTF-8");
		name = request.getParameter("name");
		age = request.getParameter("age");
		number = request.getParameter("number");
		FnumID = request.getParameter("FnumID");
		BnumID = request.getParameter("BnumID");
		area = request.getParameter("area");
		
		habit = request.getParameterValues("habit");
	%>
	
	<h2>학생 정보</h2>
	이름 : <%=name %><br>
	나이 : <%=age %><br>
	번호 : <%=number %><br>
	주민번호 : <%=FnumID %>-<%=BnumID %><br>
	취미 : <%=Arrays.toString(habit) %><br>
	지역 : <%=area %><br>


</body>
</html>
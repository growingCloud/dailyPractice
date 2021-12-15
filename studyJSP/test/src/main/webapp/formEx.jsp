<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

	<%-- form 태그로 이름 나이 전화번호 주민번호 취미(checkbox) 거주지역(select)을
		 입력받아 서버(requestEx.jsp)로 전송하기 --%>
		 
	<form action="requestEx.jsp" method="post">
	
	<fieldset>
		<legend>학생정보</legend>
		이름 : <input type="text" name="name" size="10"><br>
		나이 : <input type="text" name="age" size="10"><br>
		전화번호 : <input type="text" name="number" size="15"><br>
		주민번호 : <input type="text" name="FnumID" size="10">-
				 <input type="password" name="BnumID" size="10"><br>
			
		취미 : <label><input type="checkbox" name="habit" value="read">독서</label>
		<label><input type="checkbox" name="habit" value="walk">산책</label>
		<label><input type="checkbox" name="habit" value="swim">수영</label>
		<label><input type="checkbox" name="habit" value="clean">청소</label><br>
			
		거주지역 : <select name="area">
			<option value="Seoul">서울</option>
			<option value="Daejeon">대전</option>
			<option value="Daegu">대구</option>
			<option value="Busan">부산</option>
			</select><br>
			
			<input type="submit" value="전송">
			<input type="reset" value="취소">
			
	</fieldset>
	
	</form>

</body>
</html>
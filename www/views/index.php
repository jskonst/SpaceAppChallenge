<!DOCTYPE html>
<html lang="ru">
	<head>
		<title>Robot-RosberyPIe</title>
		<script type="text/javascript" src="http://code.jquery.com/jquery-latest.min.js"></script>
		<link href="css/milk.css" type="text/css" rel="stylesheet">
		<link href="css/my_css.css" type="text/css" rel="stylesheet">
	</head>
	<body>

		<div class="navbar">
			<div class="navbar-inner">
				<a class="brand" href="/">Robot-RosberyPI</a>
			</div>
		</div>

		<div class="container">
			<div class="row">
				<div class="span5 offset1">
					some video
				</div>
				<div class="span5">
					<form action="/create" method="POST">
						<div class="control-group">
							<div class="controls controls-row">
								<a class="btn btn-striped-light-green-right arrow" name="d"><i name="d" class="icon-16-ArrowHead-Right"></i></a>
								<a class="btn btn-striped-light-green-up arrow" name="w"><i name="w" class="icon-16-ArrowHead-Up"></i></a>
								<a class="btn btn-striped-light-green-bottom arrow" name="s"><i name="s" class="icon-16-ArrowHead-Down"></i></a>
								<a class="btn btn-striped-light-green arrow" name="a"><i name="a" class="icon-16-ArrowHead-Left"></i></a>
							</div>
						</div>
						<div class="control-group">
							<div class="controls">
								<textarea name="commands" class="span5" rows="5"></textarea>
							</div>
						</div>
						<div class="control-group">
							<div class="controls controls-row">
								<img src="secpic.php" alt="защитный код" class="span1">
								<input type="text" name="captcha" class="span2">
							</div>
						</div>
						<div class="controls-group">
							<div class="controls">
								<button type="submit" class="btn btn-large btn-primary btn-block send" name="send">Отправить</button>
							</div>
						</div>
					</form>
				</div>
			</div>
			<div class="row">
				<div class="span8 offset4">
					<?php
					if (isset($_SESSION['MESSAGE']))
					{
						echo '<p class="lead">'.$_SESSION['MESSAGE'].'</p>';
						unset($_SESSION['MESSAGE']);
					}
					?>
				</div>
			</div>
		</div>
	</body>
</html>

<script> $(document).ready(function(){
	   $(".arrow").click(function(){
			var el = $(event.target);
	 		$("textarea").val($('textarea').val() + el.attr('name')+(', '));
		});
   });
</script>
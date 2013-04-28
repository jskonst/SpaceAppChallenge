<?php
	//error_reporting(E_ALL ^ E_WARNING);
	session_start();

	/*echo'<pre>';
		print_r($_SESSION);
	echo'</pre>$_SESSION';*/

	try
	{
		require_once 'Engine.php';
		$engine = new Engine();
		$engine->run();
	}
	catch (Exception $e)
	{
		echo json_encode(
			array(
				'status' => 'error',
				'text' => $e->getMessage()
			)
		);
		die();
	}
?>
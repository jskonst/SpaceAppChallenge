<?php
class RequestWorker extends Core{
	
	public function __construct($core)
	{
		parent::__construct($core);
	}

	public function GetSegment($n)
	{
		$url = $_SERVER['REQUEST_URI'];
		$segments = explode('/', $url);
		return $segments[$n];
	}

	public function isPost()
	{
		if ($_SERVER["REQUEST_METHOD"]=="POST")
		{
			return TRUE;
		}
		return FALSE;
	}
}
?>
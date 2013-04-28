<?php
require_once 'Core.php';
require_once 'FileWorker.php';
require_once 'SecurityAgent.php';
require_once 'RequestWorker.php';

class Engine{
	
	public $fileworker;
	public $requestworker;
	public $securityagent;

	function __construct()
	{
		$this->fileworker = new FileWorker($this);
		$this->requestworker = new RequestWorker($this);
		$this->securityagent = new SecurityAgent($this);
	}

	public function run()
	{
		$route = 'action'.$this->requestworker->GetSegment(1);
		if(method_exists($this, $route == 'action'? $route = 'actionindex':$route))
		{
			$this->$route();
		}
		else
		{
			header('Location: /');
		}
	}

	public function actionindex()
	{
		$this->render('index');
	}

	public function actioncreate()
	{
		if ($this->securityagent->CheckCaptcha(isset($_POST['captcha'])?$_POST['captcha']:NULL))
		{
			$this->securityagent->WrireCommand(isset($_POST['commands'])?$_POST['commands']:NULL);
		}
		header('Location: /');
	}

	public function actionapi()
	{
		if($this->securityagent->isOurRobot())
		{
			$commands = $this->securityagent->ReadCommand();
			if (is_array($commands))
			{
				$result = array(
					'status' => 'c',
					'command' => $commands
				);
			}
			else
			{
				$result = array('status' => 'nac');
			}
			echo json_encode($result);
		}
		else
		{
			throw new Exception('Не верный ключ авторизации');
		}
	}

	public function render($view)
	{
		require_once 'views/'.$view.'.php';
	}
}
?>
<?php
class SecurityAgent extends Core{
	
	public $ac = array('w','d','s','a');
	public $c_dir = 'commands';
	public $robot_logs = 'robot_logs.txt';

	public function __construct($core)
	{
		parent::__construct($core);
	}

	public function MakeCommand($arr)
	{
		$commands = explode(',', $arr);
		foreach ($commands as $key => $value)
		{
			if( !in_array($value, $this->ac))
			{
				unset($commands[$key]);
			}
		}
		return $commands;
	}

	public function WrireCommand($arr)
	{
		$commands = $this->MakeCommand($arr);
		if ( !empty($commands))
		{
			$file_name = $this->SetCommandFileName();
			$this->getCore('fileworker')->WriteFile($file_name, implode(',', $commands));
			$this->getCore('fileworker')->WriteFileEnd($this->robot_logs, '::WRITECOMMAND::'.implode(',', $commands).'::FILE::'.$file_name);
			$_SESSION['MESSAGE'] = 'Номер ваши команды: '.$this->getCore('fileworker')->FileCount($this->robot_logs) + 1;
		}
		else
		{
			$_SESSION['MESSAGE'] = 'Команда не записанна';
		}
	}

	public function ReadCommand()
	{
		$files = scandir($this->c_dir);
		if(isset($files[2]))
		{
			$file_name = $this->GetCommandFileName($files[2]);
			$commands = explode(',', $this->getCore('fileworker')->ReadFile($file_name));
			$this->GetCore('fileworker')->RemFile($file_name);
			$this->getCore('fileworker')->WriteFileEnd($this->robot_logs, '::READCOMMAND::'.implode(',', $commands).'::FILE::'.$file_name);
			return $commands;
		}
		else
		{
			return FALSE;
		}
	}

	public function SetCommandFileName()
	{
		return $this->c_dir.'/'.time().'.txt';
	}

	public function GetCommandFileName($file)
	{
		return $this->c_dir.'/'.$file;
	}

	public function isOurRobot()
	{
		return TRUE;
	}

	public function CheckCaptcha($captcha)
	{
		if ($captcha == $_SESSION['secpic'])
		{
			return TRUE;
		}
		else
		{
			$_SESSION['MESSAGE'] = 'Капча не капча';
			return FALSE;
		}
	}
}
?>
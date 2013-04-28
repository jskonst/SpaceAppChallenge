<?php
class FileWorker extends Core{
	
	public function __construct($core)
	{
		parent::__construct($core);
	}

	public function WriteFile($file, $data)
	{
		file_put_contents($file, $data);
	}

	public function WriteFileEnd($file, $data)
	{
		file_put_contents($file, "\n".$data, FILE_APPEND);
	}

	public function ReadFile($file)
	{
		return trim(file_get_contents($file));
	}

	public function FileCount($file)
	{
		$file_arr = file($file); 
     	return count($file_arr);
	}

	public function RemFile($file)
	{
		unlink($file);
	}
}
?>
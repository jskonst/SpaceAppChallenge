<?php
class Core{
	
	protected $core;

	function __construct($core)
	{
		$this->core = $core;
	}

	public function GetCore($attr)
	{
		return $attr?$this->core->{$attr}:$this->core;
	}
}
?>
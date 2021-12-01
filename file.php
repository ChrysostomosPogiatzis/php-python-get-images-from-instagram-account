 

$dir = 'script/ig.py '.$ig_account_name;
 
                $igobj = shell_exec("python3 " . $dir);
 
                $array = json_encode($igobj);
                $check=substr($array,0, 2); 
                
                if($check=='"['){//check if python script successfuly fetch images 
                $query = "INSERT INTO `ig_images`(`image` ) VALUES ({$array} )";
                $result = $db->query($query);}

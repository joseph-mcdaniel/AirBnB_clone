# AirBnB clone, or, The Holberton B&B

### Description
The first version of this project focuses on creating a command line interpreter to be able to manage objects.
The final version will be a full web application, using this code as the core, with front-end integration (HTML/CSS templating, database storage, API).

### Synopsis
The command interpreter has specific use-cases for managing objects which limits this version's functionality to the following:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc...
* Do operations on objects (count, compute stats, etc...)
* Update attributes of an object
* Destroy an object

## Usage
To execute the command line interpreter in interactive mode run this command:
```
./console.py
```

|   **Command** |  **Definition**						 | **Example**		|
|---------------|--------------------------------------------------------------- |----------------------|
|  `help`	|  displays available commands, showsif they have documentation	 | `help`	       |
|  `quit`	|  exits the console						 | `quit`	       |
|  `EOF` 	|  exits the console						 | `EOF`		       |
|  `create` 	|  creates a new instance, saves it to JSON file, and prints id  | `create <class name>` |
|  `show`	|  prints the string representation of an instance based on the class name	|  `show <class name> <id>` |
|  `destroy`  	|  deletes an instance based on the class name and id		   		| `destroy <class name> <id>` |
|  `all`  	|  prints all string representations, can be specified by class			| `all` or `all <class name>` |
|  `update`	|  updates an instance based on the class name and id by adding or updating attribute | `update <class name> <id> <attribute name> <attribute value>` |


To run in non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb) 
$
```

### Authors

*Bobby Yang* - [Github](https://github.com/glyif) || [Twitter](https://twitter.com/bobstermyang) || [email](gaoqing.yang@holbertonschool.com)

*Joe McDaniel* - [Github](https://github.com/joseph-mcdaniel) || [Twitter](https://twitter.com/joe_w_mcdaniel) || [email](joseph.mcdaniel@holbertonschool.com)
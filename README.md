<h1>AirBnB Clone <em>(Console)</em></h3>
<hr>
<h3>What its about</h3>
<p>This repo contains the Base model of every object and classes in the AirBnB project not excluding the file storage. <br> It is a console that handles command needed for the AirBnB site. It's a dip of the toe into the ocean of AirBnB and web applications as a whole</p>
<hr>
<h3>What it does</h3>
<ul>
        <li>put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances<li>
        <li><pre>create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file<pre></li>
        <li>create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel</li>
        <li>create the first abstracted storage engine of the project: File storage.</li>
        <li>create all unittests to validate all our classes and storage engine</li>
</ul>
<hr>
<h3>Importants</h3>
<ul>
        <li>How to create a Python package</li>
        <li>How to create a command interpreter in Python using the cmd module</li>
        <li>What is Unit testing and how to implement it in a large project<li>
        <li>How to serialize and deserialize a Class<li>
        <li>How to write and read a JSON file<li>
        <li>How to manage datetime</li>
        <li>What is an UUID<li>
        <li>What is *args and how to use it</li>
        <li>What is **kwargs and how to use it</li>
        <li>How to handle named arguments in a function<li>
</ul>
<hr>
<br>
<h3>How to Use it</h3>
<p>To start it use <code>./console.py</code></p>
<p>To use it enter a the desired command on the console</p>
<h4> Examples<h4>
<ul>

        <p><strong>Interactive</strong></p>
        <li><code>
        $ ./console.py<br>
        (hbnb) help<br>
<br>
        Documented commands (type help <topic>):<br>
        ========================================<br>
        EOF  help  quit<br>
<br>
        (hbnb) <br>
        (hbnb) <br>
        (hbnb) quit<br>
        $<br>
        <code></li>
<hr>
<br>

        <p><strong>Non-nteractive</strong></p>
        <li><code>
        $ echo "help" | ./console.py<br>
        (hbnb)<br>
<br>
        Documented commands (type help <topic>):<br>
        ========================================<br>
        EOF  help  quit<br>
        (hbnb) <br>
        $<br>
        $ cat test_help<br>
        help<br>
        $<br>
        $ cat test_help | ./console.py<br>
        (hbnb)<br>

        Documented commands (type help <topic>):<br>
        ========================================<br>
        EOF  help  quit<br>
        (hbnb) <br>
        $<br>
        </code></li>
</ul>
<hr>
<br>

<h3>Tasks</h3>

<table>
        <tr>
                <td>Task 0</td>
                <td>0. README, AUTHORS</td>
        </tr>
 <tr>
                <td>Task 1</td>
                <td> Be pycodestyle compliant!</td>
        </tr>
        <tr>
                <td>Task 2</td>
                <td>Unittests</td>
        </tr>
        <tr>
                <td>Task 3</td>
                <td> BaseModel</td>
        </tr>
        <tr>
                <td>Task 4</td>
                <td>Create BaseModel from dictionary</td>
        </tr>
        <tr>
                <td>Task 5</td>
                <td>Store first object</td>
        </tr>
        <tr>
                <td>Task 6</td>
                <td>Console 0.0.1</td>
        </tr>
        <tr>
                <td>Task 7</td>
                <td>Console 0.1</td>
        </tr>
        <tr>
                <td>Task 8</td>
                <td>First User</td>
        </tr>
        <tr>
                <td>Task 9</td>
                <td>More classes!</td>
        </tr>
        <tr>
                <td>Task 10</td>
                <td>Console 1.0</td>
        </tr>
</table>

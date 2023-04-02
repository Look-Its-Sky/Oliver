<h1>Oliver</h1>
<p>This is an application to run IoT applications on with support for external modules. This is meant to be run in a Linux environment. <a href= "https://trello.com/b/gf917sHj/oliver">Here</a> is a link to the future development goals.</p>

<h3>How To Use Module System</h3>

<p>The Oliver modules are written in Python though support for more languages are coming (theres a workaround for until that happens keep reading). To add a module to Olivers system put it in the modules folder add it to the modules.txt file. To do that use verticle bars (this sign | ) to tell Oliver what you want you module to be called then put the directory after the bars. For example: <br>
<code>|module name| ./path/to/file</code>
</p>

<h3> Temporary Workaround </h3>
<p>The workaround for now would be to write a python script calling the non python executable. Example:</p>

<code>
  import os
  os.system("./path/to/executable")
</code>

Getting started with Minerva
---

1. [Make Minverva account](https://acctreq.hpc.mssm.edu)
   
2. Activate your account: sign [HIPAA form](https://hipaaforms.hpc.mssm.edu), and email [hpchelp@hpc.mssm.edu](hpchelp@hpc.mssm.edu) for activation/confirmation
   
3. Get added to a private node & lab (e.g. ask [Matt Heflin](matthew.heflin@mssm.edu) or your own lab manager for info)
   
4. [Login](https://labs.icahn.mssm.edu/minervalab/minerva-quick-start/) to Minerva through terminal:
```
   > ssh yourSinaiID@minerva.hpc.mssm.edu
   > 
   > Password: yourSinaiPassword123456 
```
   where 123456 represents the 6 digit numeric sequence obtained from your VIP Symantec token

5. ```cd``` into your project dir (i.e. ```/sc/arion/projects/guLab/yourName/```)
     if you don't have your own project folder navigate to your lab and ```mkdir yourName``` to make your own project dir, you can also   ```mkdir EMU``` or any other folders you may need

6. move your data into your project dir
```
   > scp -r yourLocalUsername@123.456.789:your/path/to/your/data sc/arion/projects/yourName/EMU
```
where 123.456.789 represents your local IP address

7. move your LFPAnalysis into your main user space (i.e. ```/hpc/users/yourSinaiID/resources/LFPAnalysis```)
   
8. to launch your jupyter notebook & run it with a sufficient amount of extra memory:
```
   > minerva-jupyter-module-web.sh -M 10000
```

9. follow this [Sinai Minerva guide](https://labs.icahn.mssm.edu/minervalab/documentation/python-and-jupyter-notebook/) to make sure your python and dependencies are all pip installed

10. you may also use ```/sc/arion/work/yourName/``` for any temp files/additional work space


---
notes:

cristybanuelos@10.125.149.1

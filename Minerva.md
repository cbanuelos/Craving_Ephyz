1. [Make Minverva account](https://acctreq.hpc.mssm.edu)
2. Activate your account: sign [HIPAA form](https://hipaaforms.hpc.mssm.edu), and email [hpchelp@hpc.mssm.edu](hpchelp@hpc.mssm.edu) for activation/confirmation
3. Get added to a private node & lab (e.g. ask [Matt Heflin](matthew.heflin@mssm.edu) or lab manager for info)
4. [Login](https://labs.icahn.mssm.edu/minervalab/minerva-quick-start/)
```
   > ssh your_userid@minerva.hpc.mssm.edu
   > 
   > Password: your_Sinai_password123456 
```
   where 123456 represents the numeric sequence obtained from your VIP Symantec token

5. ```cd``` into your project dir (i.e. ```/sc/arion/projects/guLab/Cristy/```)
     if you don't have your own project folder navigate to your lab and ```mkdir projectName``` to make your own project dir

6. move your data into your project dir
```
   > scp -r localusername@123.456.789:your/path/to/your/data sc/arion/projects/Cristy/EMU
```

8. move your LFPAnalysis into your main user space (i.e. ```/hpc/users/banuec01/resources/LFPAnalysis```)
   
10. to launch your jupyter notebook run with a sufficient amount of extra memory:
```
> minerva-jupyter-module-web.sh -M 10000
```

11. follow this [Minerva guide](https://labs.icahn.mssm.edu/minervalab/documentation/python-and-jupyter-notebook/) to make sure your python and dependencies are all pip installed

12. navigate to ```/sc/arion/work/banuec01/```


---
notes:

myUser@IP = cristybanuelos@10.125.149.1

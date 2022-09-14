def arithmetic_arranger(problems,calc=False):
    if len(problems)>5:
      return "Error: Too many problems."
    else:
        op1=[]
        op2=[]
        op=[]
        ans=[]
        lines=3
        for prob in problems:
            prob=prob.split(" ")
            if prob[0].isdigit() and prob[2].isdigit():
                pass
            else:
                return "Error: Numbers must only contain digits."
            if len(str(prob[0]))<5 and len(str(prob[2]))<5:
                op1.append(prob[0])
                op2.append(prob[2])
            else:
                return "Error: Numbers cannot be more than four digits."
            if prob[1] in ["+","-"]:
                op.append(prob[1])          
            else:
                return "Error: Operator must be '+' or '-'."
        if calc==True:
            lines=4
            for i in range(len(problems)):
                if op[i]=='+':                     
                    answer=int(op1[i])+int(op2[i])
                else:
                    answer=int(op1[i])-int(op2[i])
                ans.append(answer)                
        expr=''
        space=[]
        for j in range(len(problems)):
            if len(op1[j])>len(op2[j]):
                diff1=2
                diff2=1+len(op1[j])-len(op2[j])
                dash=len(op1[j])+2
            elif len(op1[j])<len(op2[j]):
                diff1=len(op2[j])-len(op1[j])+2
                diff2=1
                dash=len(op2[j])+2
            else:
                diff1=2
                diff2=1
                dash=len(op1[j])+2
            if calc==True:
                ans_space=dash-len(str(ans[j]))
            else:
                ans_space=0
            space.append([diff1,diff2,dash,ans_space])
        # if calc==False:
        for line in range(0,lines):
            for data in range(len(problems)):
                if line==0:
                    expr+=space[data][line]*' '
                    expr+=op1[data]
                    if data<len(problems)-1:
                        expr+="    "
                    else:
                        expr+="\n"
                elif line==1:
                    expr+=op[data]
                    expr+=space[data][line]*' '
                    expr+=op2[data]
                    if data<len(problems)-1:
                        expr+="    "
                    else:
                        expr+="\n"
                elif line==2:
                    expr+=space[data][line]*'-'
                    if data<len(problems)-1:
                        expr+="    "
                    else:
                        if lines==4:
                          expr+="\n"
                elif line==3:
                    expr+=space[data][line]*' '
                    expr+=str(ans[data])
                    if data<len(problems)-1:
                        expr+="    "
                    else:
                        pass

        return expr

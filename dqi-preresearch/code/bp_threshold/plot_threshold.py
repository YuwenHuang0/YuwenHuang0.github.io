from pathlib import Path
B=Path(__file__).resolve().parent
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

plt.rcParams.update({'font.family':['Times New Roman','Microsoft YaHei'],
 'mathtext.fontset':'stix','font.size':10.3,'axes.titlesize':11.3,
 'axes.labelsize':10.3,'xtick.labelsize':9.8,'ytick.labelsize':9.8,
 'axes.unicode_minus':False,'pdf.fonttype':42,'ps.fonttype':42})
BLUE='#245B91';LIGHT='#A5BFD9';GRAY='#7E8993';GRID='#DDE5EC'
def style(ax):
    ax.spines[['top','right']].set_visible(False)
    for edge in ['bottom','left']:ax.spines[edge].set_color('#8795A1');ax.spines[edge].set_linewidth(.65)
    ax.grid(axis='y',color=GRID,lw=.65,zorder=0);ax.set_axisbelow(True)
    ax.tick_params(length=3,color='#8795A1')

# Existing BP aggregate arrays; the right panel is a conditional theoretical conversion.
d=np.load(B/'prelim_bp.npz');fig,axes=plt.subplots(1,2,figsize=(6.2,3.4))
for key,label,col,mk in [('n300','600 比特','#A4C0DC','o'),('n1200','2400 比特','#598CB9','s'),('n4800','9600 比特',BLUE,'^')]:
    axes[0].plot(d['fracs'],d[key],marker=mk,ms=3.2,lw=1.2,color=col,label=label)
axes[0].axvline(.084,ls='--',lw=.9,color='#AD5353');axes[0].axvline(.110,ls=':',lw=.9,color=GRAY)
axes[0].text(.041,.38,'BP 门限\n约 0.084',color='#AD5353',fontsize=9.8)
axes[0].text(.109,.19,'容量参照\n约 0.110',color=GRAY,fontsize=9.8,ha='right')
axes[0].legend(loc='lower left',frameon=False,fontsize=9.2)
axes[0].set(xlim=(.028,.113),ylim=(-.02,1.05),xlabel='出错比特比例',ylabel='BP 恢复成功率',title='(a) 不同纠错码长度的仿真')
rho=np.linspace(0,.5,400);axes[1].plot(rho,.5+np.sqrt(rho*(1-rho)),color=BLUE,lw=1.6)
for x,text,color,pos in [(.084,'BP 门限换算：77.7%','#AD5353',(.18,.65)),(.110,'容量参照换算：81.3%',BLUE,(.17,.9))]:
    y=.5+np.sqrt(x*(1-x));axes[1].scatter([x],[y],s=27,color=color,zorder=3)
    axes[1].annotate(text,(x,y),xytext=pos,fontsize=9.2,color=color,arrowprops={'arrowstyle':'-','lw':.7,'color':color})
axes[1].text(.25,.54,r'$J_{\rm ref}=\frac{1}{2}+\sqrt{\rho(1-\rho)}$',ha='center',fontsize=12,color=BLUE)
axes[1].set(xlim=(0,.5),ylim=(.45,1.03),xlabel='可恢复的错误比例 ρ',ylabel='换算的平均满足约束比例',title='(b) DQI 原文条件下的换算')
for ax in axes:style(ax)
fig.subplots_adjust(left=.1,right=.99,top=.86,bottom=.24,wspace=.5)
fig.text(.5,.06,'右图为门限到解质量的条件换算，不是有限长度仿真的实际 DQI 输出或严格界。',ha='center',fontsize=9.8,color='#52616E')
fig.savefig(B/'bp_threshold.pdf');plt.close(fig)

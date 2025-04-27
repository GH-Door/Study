import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
"""
각 시각화 함수
"""

# bar_plot 함수    
def bar_plot(df, x_col, y_col, figsize=(10, 6), hue=None, palette="Blues_r", rotation=None, title=None, xlabel=None, ylabel=None):
     plt.figure(figsize=figsize)
     
     if hue: # hue 지정
        sns.barplot(x=x_col, y=y_col, hue=hue, data=df, palette=palette)
     else: # hue 지정 X
        sns.barplot(x=x_col, y=y_col, data=df, palette=palette)

     plt.xticks(rotation=rotation)
     plt.title(title)
     plt.xlabel(xlabel)
     plt.ylabel(ylabel)
     plt.show()

# box_plot 함수
def box_plot(df1, col, df2=None, figsize=(8, 6), color1='skyblue', color2='salmon', title=None):
    plt.figure(figsize=figsize)

    if df2 is None:
        # 단일 데이터프레임 boxplot
        sns.boxplot(y=df1[col], color=color1)  # 개별일 때는 color1 (기본값 skyblue)
        plt.ylabel(col)
        plt.title(title if title else f'{col} (Box Plot)')
    else:
        # 두 데이터프레임 비교 boxplot
        plt.subplot(1, 2, 1)
        sns.boxplot(y=df1[col], color=color1)  # 첫 번째 그룹은 color1
        plt.ylabel(col)
        plt.title(f'Group 1 - {col}')

        plt.subplot(1, 2, 2)
        sns.boxplot(y=df2[col], color=color2)  # 두 번째 그룹은 color2
        plt.ylabel(col)
        plt.title(f'Group 2 - {col}')

        plt.suptitle(title if title else f'{col} Comparison (Box Plot)', fontsize=12)

    plt.show()

# hist_plot 함수
def hist_plot(df1, col, df2=None, figsize=(8, 6), bins=30, alpha=0.6, color1='skyblue', color2='salmon', label1=None, label2=None, title=None):
    plt.figure(figsize=figsize)

    # 개별 데이터 프레임
    sns.histplot(df1[col], kde=True, bins=bins, alpha=alpha, color=color1, label=label1 if label1 else ('Group 1' if df2 is not None else None))
    
    if df2 is not None: # 두 그룹 비교
        sns.histplot(df2[col], kde=True, bins=bins, alpha=alpha, color=color2, label=label2 if label2 else 'Group 2')
        plt.legend()  # 두 그룹일 때만 범례 표시

    plt.title(title if title else f'{col} Distribution (Histogram + KDE)')
    plt.xlabel(col)
    plt.show()

# line_plot 함수
def line_plot(df, x_col, y_col, hue=None, figsize=(10, 6), palette=None, marker='o', linewidth=2, rotation=None, title=None, xlabel=None, ylabel=None):
    plt.figure(figsize=figsize)
    
    # hue가 None이면 일반 lineplot, hue가 있으면 그룹별 lineplot
    sns.lineplot(data=df, x=x_col, y=y_col, hue=hue, palette=palette, marker=marker, linewidth=linewidth)
    plt.xticks(rotation=rotation)  
    plt.title(title if title else f'{y_col} by {x_col} (Line Plot)')  
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    if hue: # hue가 있을 경우 범례 추가
        plt.legend(title=hue)
    plt.show()

# heatmap 함수
def heatmap(df, figsize=(10, 6), target_col=None, threshold=0.4, annot=True, fmt='.2f', cmap='Blues', annot_kws={"size": 12}, cbar=True, title=None):
    corr = df.select_dtypes(include=['number']).corr() # 숫자형 데이터 타입

    if target_col: # 타겟 컬럼과의 상관관계만 추출
        corr = corr[[target_col]].sort_values(by=target_col, ascending=False)
        corr = corr[abs(corr[target_col]) >= threshold].dropna()
        
        title = title or f"'{target_col}'과의 상관관계 (≥ {threshold})"
        plt.figure(figsize=(4, len(corr) * 0.6))
        sns.heatmap(corr.T, annot=annot, fmt=fmt, cmap=cmap, annot_kws=annot_kws, cbar=cbar)
    
    else: # 전체 상관관계 매트릭스
        title = title or "전체 상관관계 히트맵"
        plt.figure(figsize=figsize)
        sns.heatmap(corr, annot=annot, fmt=fmt, cmap=cmap, annot_kws=annot_kws, cbar=cbar)

    plt.title(title)
    plt.show()




    
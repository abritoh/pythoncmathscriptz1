# -*- coding: utf-8 -*-
# =============================================================================
# Script: 31-python-math.py
# Python 3.8.2
# (c) abritoh - 2020-08
# =============================================================================
 
import os
import math
import cmath
import numpy
import random
import matplotlib.pyplot as plt
 
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    return
 
def fn_math() :
    print("n++++++++++++++++++++ fn_math +++++++++++++++++++++")
     
    print("Constantes del módulo math")
    CTE_PI = math.pi    # 3.141592...
    CTE_E = math.e      # 2.718281
    CTE_TAU = math.tau    # 6.283185 = 2 * PI
    CTE_INF = math.inf    # infinite
    CTE_NAN = math.nan    # nan = not a number
     
    print(" CTE_PI={}; CTE_E={} n CTE_TAU={} CTE_INF={} CTE_NAN={}".format(CTE_PI, CTE_E, CTE_TAU, CTE_INF, CTE_NAN) )
     
    a = 123.321
    b = 789.543
     
    # ceil round-up
    a_ceil = math.ceil(a)
    b_ceil = math.ceil(b)
    print(" a={}; b={};  a_ceil={};  b_ceil={}".format(a, b, a_ceil, b_ceil) )
     
    # floor round-down
    a_floor = math.floor(a)
    b_floor = math.floor(b)
    print(" a={}; b={};  a_floor={}; b_floor={}".format(a, b, a_floor, b_floor) )
     
    # truncate --> integer part
    a_trunc = math.trunc(a)
    b_trunc = math.trunc(b)
    print(" a={}; b={};  a_trunc={}; b_trunc={}".format(a, b, a_trunc, b_trunc) )    
     
    # abs
    a_neg = -123456.789
    a_abs = math.fabs(b)
    print(" a_neg={}; a_abs={}".format(a_neg, a_abs) )
     
    n, k = 20, 2
     
    # factorial: 5! = 5 x 4 x 3 x 2 x 1
    f1 = math.factorial(5)
    # permutacion => n! / (n - k)!
    p1 = math.perm(n, k)
    # combinación => n! / (k! * (n - k)!)
    c1 = math.comb(n, k)
    print(" n={}; k={}; f1={}; p1={}; c1={} n".format(n, k, f1, p1, c1) )
     
    # mod and fmod
    print(" 20%2 = {}".format( 20%2  ) )
    print(" 10%3 = {}".format( 10%3  ) )
    print(" math.fmod(10, 3) = {}".format( math.fmod(10, 3) ) )
    print(" math.fmod(10, 3) = {} n".format( math.fmod(10, 2.2)  ) )
     
    # sum, fsum and prod
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list2 = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]    
    sum1 = sum(list1)
    fsum1 = math.fsum(list1)
    fsum2 = math.fsum(list2)
    prod1 = math.prod(list1)
    print(" sum1 = {}; fsum1 = {}; fsum2 = {}, prod1 = {}".format( sum1, fsum1, fsum2, prod1 ) )
     
    # isinf, isnan --> nan = Not A Number    
    print(" isinf(n1)={}; isnan(n1)={}".format( math.isinf(math.inf), math.isnan(math.nan) ) )
     
    # exponential and logaritmic
    x = 3
    y = 5   
    dict1 = {
        "expx"  : math.exp(x),
        "logx2" : math.log(x, 2),
        "logx10": math.log(x, 10),
        "log2"  : math.log2(x),
        "log10" : math.log10(x),
        "pow1"  : math.pow(x, y),
        "sqr1"  : math.sqrt(x)
    }    
    print(" dict1 => ", dict1 )    
     
    # trigonometric functions    
    x = math.pi
    y = math.pi / 6
    dict2 = {
        "sin"  : math.sin(x),
        "cos" : math.cos(x),
        "tan": math.tan(x),
        "asin"  : math.asin(0),
        "acos" : math.acos(0),
        "atan"  : math.atan(0),        
    }    
    print(" dict2 => ", dict2 )
     
    return
 
 
def fn_cmath() :
    print("n++++++++++++++++++++ fn_cmath +++++++++++++++++++++")
    print("Constantes del módulo cmath")
    CTE_PI = cmath.pi    # 3.141592...
    CTE_E = cmath.e      # 2.718281
    CTE_TAU = cmath.tau    # 6.283185 = 2 * PI
    CTE_INF = cmath.inf    # infinite
    CTE_INFJ = cmath.infj    # infinite for imaginary part
    CTE_NAN = cmath.nan    # not a number
    CTE_NANJ = cmath.nanj    # not a imaginary number
     
    print(" CTE_PI={} CTE_E={} n CTE_TAU={} CTE_INFJ={} CTE_NANJ={}".format(CTE_PI, CTE_E, CTE_TAU, CTE_INFJ, CTE_NANJ) )
     
    z1 = complex(2.0, 3.0)
    z2 = 4.0 + 5.0j
    z3 = -6.2 -2.6j
    z4 = complex(-10, -9)
    print(z1, z2, z3, z4)
     
    print("n **********  Extrae la parte real e imaginaria de cada número complejo")
    listz_1 = [z1, z2, z3, z4]
    for z in listz_1 :
        print(" {} ........ => real[z] = {},  imag[z]={}".format(z, z.real, z.imag) )
    #end-for    
     
    # -------------------------------------------------------------------------
    # genera 2 listas de números-reales aleatorios enteros 
    # -------------------------------------------------------------------------    
    # forma 1, utilizando random.randint(...)
    list_int1 = []
    for i in range(0, 10):
        random_integer = random.randint(-10, 10)
        list_int1.append(random_integer)
    #end-for
    print("nlist_int1", list_int1)
     
    # forma 2, utilizando random.sample(...)
    list_int2 = random.sample(range(-10, 10), 10)
    print("list_int2", list_int2)
    # -------------------------------------------------------------------------
     
    complex_numbers  = []
    for (n1, n2) in zip(list_int1, list_int2) :
        complex_numbers.append(complex(n1, n2))
    #end-for
     
    list_x = [x.real for x in complex_numbers]     
    list_y = [x.imag for x in complex_numbers]    
     
    # -------------------------------------------------------------------------    
    # crea el grafico de los pares (x, y) de los numeros complejos generados aleatoriamente
    # -------------------------------------------------------------------------
    plt.title("Números Complejos (rectángular) : Z = re[Z] + jImg[Z]")
    fig = plt.gcf()
    fig.set_size_inches(10, 10)    
     
    #plt.xlabel("x = Re [z]")
    #plt.ylabel("y = Img [z]")    
    # establece límite de los ejes x e y
    #plt.xlim(0, 20)
    #plt.ylim(0, 20)
     
    # genera el grafico de puntos    
    plt.scatter(list_x, list_y, color="blue")
     
    for z in complex_numbers :
        plt.text(z.real, z.imag, "{}".format(z), color="red")
    #end-for
     
    for z in complex_numbers :
        plt.plot([0, z.real], [0, z.imag])
    #end-for
     
    # coloca los ejes en (0,0)
    ax = plt.gca()
    ax.spines['left'].set_position("zero")
    ax.spines['bottom'].set_position("zero")
     
    # elimina los ejes right y top
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')    
     
    plt.grid()
    plt.show()
    # -------------------------------------------------------------------------
     
     
    # -------------------------------------------------------------------------
    # Crea el grafico en de números complejos en su forma polar
    #   El número complejo en su forma polar es: Z = |Z| z_angulo
    #   donde |z| = sqrt(x**2 + y**2) y z_angulo = arctan(y/x)
    #   siendo y, x las componentes real (x) e imaginaria (y) de "Z"
    # -------------------------------------------------------------------------
     
    list_z_polar = [cmath.polar(z) for z in complex_numbers]
    list_z_abs   = [abs(z) for z in complex_numbers]
    list_z_angle = [cmath.phase(z) for z in complex_numbers]
     
    print("********** Números complejos en su forma polar")
    #print(list_z_polar)
    #print(list_z_abs)
    #print(list_z_angle)
 
    plt.axes(projection = "polar")
    fig = plt.gcf()
    fig.set_size_inches(10, 10)    
    plt.title("Números Complejos (polar) : Z = abs(z), ángulo(z) n")
    #>>plt.xlabel("n x = Re [z]")
    #>>plt.ylabel("y = Img [z]")
     
    for z in complex_numbers:
        plt.polar([0, cmath.phase(z)], [0, abs(z)], marker="o")
    #end-for
    
    ax = plt.gca()
    ax.grid(True) # gca = get current axes
     
    # itera por cada numero complejo y agrega una etiqueta con el valor de "z"
    # x = |z| * cos(angulo), y = |z| * sin(angulo)
    for z in complex_numbers:       
        angle = cmath.phase(z)
        abs_z = abs(z)
        angle_degre =  round(math.degrees(angle))
        angle_degre = angle_degre if angle_degre > 0 else 360 - abs(angle_degre)
        abs_z_round = round(abs_z, 2)
        ax.annotate("{}<{}".format(abs_z_round, angle_degre), xy=(angle, abs_z), color="red", xycoords="data")
    #end-for    
     
    ax.set_thetamin(0)
    ax.set_thetamax(360)
     
    plt.show()
     
    return
 
def main() :
    cls()
    fn_math()
    fn_cmath()
    return
 
#######################################
# main
#######################################
main()
############ END ######################

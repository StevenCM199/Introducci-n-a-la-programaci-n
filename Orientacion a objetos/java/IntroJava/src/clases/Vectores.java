/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package clases;

import java.util.Scanner;

public class Vectores {
   
    public Vectores(){}
        public void imprimirArray(int[] vector){
       /* for(int contador = 0; contador < vector.length; contador++){
            System.out.println("El valor del array en la posición " + contador + " es " + vector[contador]);
        }*/
        for(int valor: vector){
            System.out.println("El valor es " + valor);
        }
    }
    public int[] llenarArray(){
        int[] vector = new int[5];
        Scanner entrada = new Scanner(System.in);
        for(int contador = 0; contador < vector.length; contador++){
            System.out.println("Ingrese el valor del array para la posición " 
                                + contador);
            vector[contador] = entrada.nextInt();
        }
        return vector;
    }
    public int[] sumarArrays(int[] vector1, int[] vector2){
        int[] vectorSuma = new int[vector1.length];
        for(int contador = 0; contador < vector1.length; contador++){
            vectorSuma[contador] = vector1[contador] + vector2[contador];
        }
        return vectorSuma;
    }    
    public static void main(String[] args){
        Vectores vect = new Vectores();
        System.out.println("Llenar valores del array 1");
        int[] vector1 = vect.llenarArray();
        System.out.println("Llenar valores del array 2");
        int[] vector2 = vect.llenarArray();   
        int[] vector3 = vect.sumarArrays(vector1, vector2);  
        vect.imprimirArray(vector3);
    }
}

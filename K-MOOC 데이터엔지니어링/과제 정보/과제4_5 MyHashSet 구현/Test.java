package kr.kmooc.dataEngineering.homework4_5;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Random;
import java.util.Set;


public class Test 
{
    public static void main( String[] args )
    {
    	boolean isPass;
    	System.out.println("<Assignment 4-5>");
    	List<Integer> arrayList = new ArrayList<Integer>();
    	Random r = new Random();
    	for(int i = 0 ; i < 1000 ; i++)
    		arrayList.add(r.nextInt(1000));
    	
    	Set<Integer> testHashSet = new HashSet<Integer>();
    	Set<Integer> yourHashSet = new MyHashSet<Integer>();
    	//add() test
    	isPass = true;
    	for(Integer val : arrayList) {
    		testHashSet.add(val);
    		yourHashSet.add(val);
    	}
    	if(!testHashSet.equals(yourHashSet))
    		isPass = false;
    	System.out.println("add test: "+ isPass);
    	
    	
    	//size(),isEmpty() test
    	System.out.println("size test: " + (testHashSet.size() == yourHashSet.size()));
    	System.out.println("isEmpty test: " + (testHashSet.size() == yourHashSet.size()));
    	
    	//remove() test
    	isPass = true;
    	for(int i = 0 ; i < 100 ; i++) {
    		Integer removeNum = r.nextInt(1000);
    		yourHashSet.remove(removeNum);
    		testHashSet.remove(removeNum);
    	}
    	if(!testHashSet.equals(yourHashSet))
    		isPass = false;
    	
    	System.out.println("remove test: " + isPass);
    	
    	//contains() test
    	isPass = true;
    	for(int i = 0 ; i < 100 ; i++) {
    		Integer randomNum = r.nextInt(1000);
    		if(testHashSet.contains(randomNum) != yourHashSet.contains(randomNum)) {
    			isPass = false;
    			break;
    		}
    	}
    	System.out.println("contains test: " + isPass);
    	
    	
    	//addAll() test
    	isPass = true;
    	try {
    		Set<Integer> tmpSet = new HashSet<Integer>();
    		tmpSet.addAll(testHashSet);
    		tmpSet.addAll(yourHashSet);
    		if(!tmpSet.equals(yourHashSet) && !tmpSet.equals(yourHashSet))
    			throw new Exception();
    		
    	}catch(Exception e){
    		isPass = false;
    		System.out.println("addAll test: "+ isPass );
    	}
    	System.out.println("addAll test: "+ isPass);
    	
    	//retainAll() test
    	isPass = true;
    	try {
    		Set<Integer> tmpSet = new HashSet<Integer>();
    		tmpSet.addAll(testHashSet);
    		tmpSet.retainAll(yourHashSet);
    		if(!tmpSet.equals(yourHashSet) && !tmpSet.equals(testHashSet))
    			throw new Exception();
    		
    	}catch(Exception e) {
    		isPass = false;
    		}
    		
    	System.out.println("retainAll test: "+ isPass);
    	
    	//iterator() test
    	isPass = true;
    	Iterator<Integer> setIterator = testHashSet.iterator();
    	Iterator<Integer> yourIterator = yourHashSet.iterator();
    	try {
    		Set<Integer> testSet1 = new HashSet<>();
    		Set<Integer> testSet2= new HashSet<>();
    		while(setIterator.hasNext())
    			testSet1.add(setIterator.next());
    		while(yourIterator.hasNext())
    			testSet2.add(yourIterator.next());
    		
    		if(!testSet1.equals(testSet2))
    			throw new Exception();
    	}catch(Exception e) {
    		isPass = false;
    	}
    	System.out.println("iterator test: " + isPass);
    
    	
    	//removeAll() test
    	isPass = true;
    	try {
    		Set<Integer> tmpSet = new HashSet<Integer>();
    		tmpSet.addAll(testHashSet);
    		tmpSet.removeAll(yourHashSet);
    		
    		if(tmpSet.size() != 0)
    			throw new Exception();
    		
    	}catch(Exception e){
    		isPass = false;
    		
    	}
    	System.out.println("removeAll test: "+ isPass);
    	//clear() test
    	yourHashSet.clear();
    	testHashSet.clear();
    	System.out.println("clear test: " + (yourHashSet.isEmpty() && testHashSet.isEmpty()));
    	
    }
}

package kr.kmooc.dataEngineering.homework2_3;

import java.util.AbstractSequentialList;
import java.util.Collection;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;
import java.util.Queue;
public class MyLinkedList<E> implements List<E>, Queue<E>{
    private MyNode<E> first;
    private MyNode<E> last;
    private int size;

    public MyLinkedList() {
        first = null;
        last = null;
        size = 0;
    }

    public MyLinkedList(Collection<? extends E> c) {
        this();
        for (E value : c) {
            add(value);
        }
    }

    @Override
    public String toString() {
        if (size == 0) {
            return "[]";
        }

        String result = "[";
        result += first.getItem();
        MyNode<E> cursor = first.getNext();
        while (cursor != null) {
            result += ", " + cursor.getItem();
            cursor = cursor.getNext();
        }
        result += "]";
        return result;
    }

    @Override
    public boolean offer(E e) {
// TODO Auto-generated method stub
        return false;
    }
    @Override
    public E remove() {
// TODO Auto-generated method stub
        return null;
    }
    @Override
    public E poll() {
// TODO Auto-generated method stub
        return null;
    }
    @Override
    public E element() {
// TODO Auto-generated method stub
        return null;
    }
    @Override
    public E peek() {
// TODO Auto-generated method stub
        return null;
    }
    @Override
    public int size() {
        return size;
    }
    @Override
    public boolean isEmpty() {
        return size == 0;
    }

    @Override
    public boolean contains(Object o) {
// TODO Auto-generated method stub
        return false;
    }
    @Override
    public Iterator<E> iterator() {
// TODO Auto-generated method stub
        return null;
    }
    @Override
    public Object[] toArray() {
// TODO Auto-generated method stub
        return null;
    }
    @Override
    public <T> T[] toArray(T[] a) {
// TODO Auto-generated method stub
        return null;
    }
    @Override
    public boolean add(E e) {
        if (first == null) {
            // 비어 있을 때
            MyNode<E> newNode = new MyNode<E>(null, e, null);
            first = newNode;
            last = newNode;
            size++;
        } else {
            // 비어 있지 않을 때
            MyNode<E> newNode = new MyNode<E>(last, e, null);
            last.setNext(newNode);
            last = newNode;
            size++;
        }
        return true;
    }

    @Override
    public boolean remove(Object o) {
// TODO Auto-generated method stub
        return false;
    }
    @Override
    public boolean containsAll(Collection<?> c) {
// TODO Auto-generated method stub
        return false;
    }
    @Override
    public boolean addAll(Collection<? extends E> c) {
// TODO Auto-generated method stub
        return false;
    }
    @Override
    public boolean addAll(int index, Collection<? extends E> c) {
// TODO Auto-generated method stub
        return false;
    }
    @Override

    public boolean removeAll(Collection<?> c) {
// TODO Auto-generated method stub
        return false;
    }
    @Override
    public boolean retainAll(Collection<?> c) {
// TODO Auto-generated method stub
        return false;
    }
    @Override
    public void clear() {
// TODO Auto-generated method stub
    }
    @Override
    public E get(int index) {
// TODO Auto-generated method stub
        return null;
    }
    @Override
    public E set(int index, E element) {
// TODO Auto-generated method stub
        return null;
    }
    @Override
    public void add(int index, E element) {
// TODO Auto-generated method stub
    }
    @Override
    public E remove(int index) {
// TODO Auto-generated method stub
        return null;
    }
    @Override
    public int indexOf(Object o) {
// TODO Auto-generated method stub
        return 0;
    }
    @Override
    public int lastIndexOf(Object o) {
// TODO Auto-generated method stub
        return 0;
    }
    @Override
    public ListIterator<E> listIterator() {
// TODO Auto-generated method stub
        return null;
    }
    @Override
    public ListIterator<E> listIterator(int index) {
// TODO Auto-generated method stub
        return null;
    }
    @Override
    public List<E> subList(int fromIndex, int toIndex) {
// TODO Auto-generated method stub
        return null;
    }
}

package kr.kmooc.dataEngineering.homework2_3;
public class MyNode<E> {
    private E item;
    private MyNode<E> prev;
    private MyNode<E> next;

    public MyNode(MyNode<E> prev, E item, MyNode<E> next) {
        this.prev = prev;
        this.item = item;
        this.next = next;
    }

    public E getItem() {
        return item;
    }

    public void setItem(E item) {
        this.item = item;
    }

    public MyNode<E> getPrev() {
        return prev;
    }

    public void setPrev(MyNode<E> prev) {
        this.prev = prev;
    }

    public MyNode<E> getNext() {
        return next;
    }

    public void setNext(MyNode<E> next) {
        this.next = next;
    }

    @Override
    public String toString() {
        return item.toString();
    }
}
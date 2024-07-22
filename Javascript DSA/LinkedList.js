class Node{
    constructor(element){
        this.element= element;
        this.next = null;
    }
}

class LinkedList{
    constructor(){
        this.head = null
        this.size = 0
    }

    add(element){
        var node = new Node(element)

        var current;
        if (this.head== null) {
            this.head = node
            console.log(this.head)
        }else{
            current = this.head
            while(current.next){
                current= current.next
            }current.next = node
            console.log(current)
        }this.size+=1;
    }
}


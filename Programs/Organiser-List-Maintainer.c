/*
Let in one conference, at the time of registration process the registration desk prepare one master linked list
 to register the participant irrespective of their type. Let the type of participants are Student, Guest, Organizing team, Delegate. 
a.	Name(String)
b.	Type of Participant (Char: For Student- ‘S’, Guest - ’G’, Organizing team - ‘O’, Delegate - ‘D’)
c.	Phone number (10 digit int array)

*/
#include <stdio.h>
#include <stdlib.h>

struct database
{
    char name[30];
    long int ph_no;
    char type;
    struct database *next;
};

void output(struct database *q)
{
    printf("Name: %s\n", q -> name);
    printf("Type: %c\n", q -> type);
    printf("Phone number: %ld\n", q -> ph_no);
}

void display(struct database *hs , struct database *hg , struct database *ho , struct database *hd)
{
    struct database *ptr = hs;
    printf("\nStudents :\n");
    int i = 1;
    while (ptr != NULL)
    {
        printf("\nStudent %d:\n", i);
        output(ptr);
        ptr = ptr -> next;
        i++;
    }

    ptr = hg;
    printf("\nGuest :\n");
    i = 1;
    while (ptr != NULL)
    {
        printf("\nGuest %d:\n", i);
        output(ptr);
        ptr = ptr -> next;
        i++;
    }

    ptr = ho;
    printf("\nOrganizing Team :\n");
    i = 1;
    while (ptr != NULL)
    {
        printf("\nOrganizing Team %d:\n", i);
        output(ptr);
        ptr = ptr -> next;
        i++;
    }

    ptr = hd;
    printf("\nDelegate :\n");
    i = 1;
    while (ptr != NULL)
    {
        printf("\nDelegate %d:\n", i);
        output(ptr);
        ptr = ptr -> next;
        i++;
    }
}

void LinkListSep(struct database **h ,struct database **hs , struct database **hg , struct database **ho , struct database **hd)
{
    struct database *ptr , *temp;

    for (ptr = *h ; ptr != NULL;)
    {
        temp = malloc(sizeof(struct database)) ;
        *temp = *ptr;
        if(ptr -> type == 'S' || ptr -> type == 's')
        {
            ptr -> next = *hs;
            *hs = ptr; 
        }
        else if(ptr -> type == 'G' || ptr -> type == 'g')
        {
            ptr -> next = *hg;
            *hg = ptr; 
        }
        else if(ptr -> type == 'O' || ptr -> type == 'o')
        {
            ptr -> next = *ho;
            *ho = ptr; 
        }
        else
        {
            ptr -> next = *hd;
            *hd = ptr; 
        }
        ptr = temp -> next;
        *h = ptr;
    }
}

void insert(struct database **h)
{
    struct database *curr;
    curr = malloc(sizeof(struct database));
    printf("Enter participant info - \n");
    printf("Name : ");
    scanf("%s", curr->name);
    printf("Type : ");
    scanf(" %c", &curr->type);
    printf("Phone number : ");
    scanf("%ld", &curr->ph_no);
    curr->next = NULL;

    if (*h == NULL)
        *h = curr;
    else
    {
        curr->next = *h; 
        *h = curr;
    }
}

int main()
{

    printf("Welcome\n\n");
    struct database *head , *hs , *hg , *ho , *hd;
    head = hs = hg = ho = hd = NULL;
    char choice;
    
    while (1)
    {
        printf("\nDo you want to add more participants ? (y/n) : ");
        scanf(" %c", &choice);
        if (choice == 'n')
            break;
        insert(&head);
    }
    
    LinkListSep(&head , &hs , &hg , &ho , &hd);
    display(hs , hg , ho , hd);
    
    if(head == NULL)
        printf("\nMaster Link List Destroyed!\n");

    return 0;
}

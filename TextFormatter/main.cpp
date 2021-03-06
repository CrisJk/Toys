/**
在使用pdf阅读英文文献时，偶尔会需要大段翻译，有些时候将文献复制粘贴到翻译软件中时，复制下来的文字会保留原本的换行符，影响翻译准确度。本代码自动去除这些换行符。
使用方法:在任意一款c++编译器中编译运行本代码，将文档粘贴到控制台即可
**/
#include <iostream>
#include <string>
using namespace std;

int main()
{
    string str ;
    string answer;
    string pre = "endline" ;
    while(getline(cin,str)){
        if(str.length() == 0 ){
            break ;
        }

        if(pre == "endline"){
            answer += " "+str;
        }
        else{
            answer += str;
        }
        //判断连接符
        if(answer[answer.length()-1] == '-'){
            answer.pop_back() ;
            pre = "notendline" ;
        }
        else{
            pre = "endline" ;
        }

    }
    cout<<"======================"<<endl;
    cout<<answer<<endl;
    return 0;
}

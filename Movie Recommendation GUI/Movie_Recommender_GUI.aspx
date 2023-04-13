<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Movie_Recommender_GUI.aspx.cs" Inherits="Movie_Recommendation_GUI.Movie_Recommender_GUI" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>CSE 573 Group 31 Movie Recommendation System Web Page</title>
    <style type="text/css">
        div{
            font-family: 'Times New Roman';
        }
    </style>
    </head>
<body>
    <form id="form1" runat="server">
        <div>
            <h1>CSE 573 Group 31 Movie Recommendation System</h1>
            <h4>Group Members: Sai Tiruchinapalli, Saif Masood, Daljit Bhalla, Aishwarya Jagarapu, Abhi Teja Veresi,
                Nanda Sai Varma Gadidesi</h4>
            <br />
            <asp:Label ID="Label1" runat="server" Text="Username: "></asp:Label> 
            <asp:TextBox ID="TextBox1" runat="server"></asp:TextBox>
            <asp:Label ID="Label2" runat="server" Text="Password: "></asp:Label> 
            <asp:TextBox ID="TextBox2" runat="server"></asp:TextBox>
            <asp:Button ID="Button1" runat="server" Text="Login" />
            <br />
            <p>Top 5 Movie Recommendations</p>
            <asp:Image ID="Image1" runat="server" />
            <asp:Label ID="Label3" runat="server" Text="Movie 1"></asp:Label>
            <br />
            <asp:Image ID="Image2" runat="server" />
            <asp:Label ID="Label4" runat="server" Text="Movie 2"></asp:Label>
            <br />
            <asp:Image ID="Image3" runat="server" />
            <asp:Label ID="Label5" runat="server" Text="Movie 3"></asp:Label>
            <br />
            <asp:Image ID="Image4" runat="server" />
            <asp:Label ID="Label6" runat="server" Text="Movie 4"></asp:Label>
            <br />
            <asp:Image ID="Image5" runat="server" />
            <asp:Label ID="Label7" runat="server" Text="Movie 5"></asp:Label>
            <br />
        </div>
    </form>
</body>
</html>

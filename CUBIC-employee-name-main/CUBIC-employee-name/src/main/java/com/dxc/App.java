package com.dxc;

import java.sql.*;
import java.util.ArrayList;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.dxc.Entities.Employee;
import com.dxc.Entities.RequestDetails;

public class App implements RequestHandler<RequestDetails, ArrayList<Employee>> {
    
    @Override
    // entry point for the lambda function

    //RequestDetails not needed. Test lambda without RequestDetails once.
    // requestDetails is the POJO representation of the query parameters
    public ArrayList<Employee> handleRequest(RequestDetails requestDetails, Context context) {

        // initialize the list of employees to return through the API
        
        ArrayList<Employee> employees = new ArrayList<>();

        try {

            // Populate the list of employees
            queryResultToEmployeeList(requestDetails, employees);

        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
       
        // Return the list of employees
        return employees;
    }
   
    /**
     * @param requestDetails
     * @param responseDetails
     * @throws SQLException
     */

     //Function where the Employee object gets populated.
    private void queryResultToEmployeeList(RequestDetails requestDetail, ArrayList<Employee> employees)
            throws SQLException {

        // Getting the connection to the database
        Connection conn = getConnection();
        
        // Creating statement that holds the query and the result after executing the query
        
        // Create the query for the statement by passing the query parameters
        ResultSet result = createQuery(requestDetail, conn);
       
        // Loop for all the records in the result
        while (result.next()) {

            // add a new employee to the employee list
            // by constructing a new employee from the information obtained from the
            // resultset
           
            employees.add(new Employee(
                //add a.employee_id, employee_name,
                    result.getString("employee_id"),
                    result.getString("employee_name")));
        }
    }

    /**
     * @param request
     * @return
     */
    private ResultSet createQuery(RequestDetails request, Connection conn) throws SQLException{

        //initial query string
        String query = "select employee_id, employee_name from employees_table where employee_name like ?";
        PreparedStatement stmt = conn.prepareStatement(query);
        stmt.setString(1,"%"+ request.getemployeeName()+"%"); 
        //check if the request has any parameters as there will e no input request we don't need the if block to be executed.
        //if request has no paramters, execute only the initial query
        return stmt.executeQuery();
    }

    /**
     * @return Connection to the database
     * @throws SQLException
     */
    //create a connection to the database
    private Connection getConnection() throws SQLException {

        //Retriving values from Lambda enivironment variables
        String hostname = System.getenv("db_endpoint");
        String db_name = System.getenv("db_name");
        String db_user_name = System.getenv("username");
        String db_pwd = System.getenv("password");
        
        Connection conn = DriverManager.getConnection("jdbc:mysql://" + hostname +"/" + db_name, db_user_name, db_pwd);
        return conn;
    }

}
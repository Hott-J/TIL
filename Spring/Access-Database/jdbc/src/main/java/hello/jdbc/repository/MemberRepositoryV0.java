package hello.jdbc.repository;

import hello.jdbc.connection.DBConnectionUtil;
import hello.jdbc.domain.Member;
import lombok.extern.slf4j.Slf4j;

import java.sql.*;

/**
 * JDBC -DriverManager 사용
 */
@Slf4j
public class MemberRepositoryV0 {

    public Member save(Member member) throws SQLException {
        String sql = "insert into member(member_id, money) values (?, ?)";

        Connection con = null;
        PreparedStatement pstmt = null;

        try {
            con = getConnection();
            pstmt = con.prepareStatement(sql);

            // sql values ?, ? setting
            pstmt.setString(1, member.getMemberId());
            pstmt.setInt(2, member.getMoney());
            pstmt.executeUpdate(); // 업데이트했을때 영향받은 row 수만큼 반환됨
            return member;
        } catch (SQLException e) {
            log.error("db error", e);
            throw e;
        } finally {
            close(con, pstmt, null);
        }
    }

    // PreparedStatement는 파라미터 바인딩이 가능하고 Statement는 그냥 sql 날림
    // 사용한 자원들을 전부 닫아줘야한다
    private void close(Connection con, Statement stmt, ResultSet rs) {

        if (rs != null) {
            try {
                rs.close(); // SQLException
            } catch (SQLException e) {
                log.info("error", e);
            }
        }

        if (stmt != null) {
            try {
                stmt.close(); // SQLException
            } catch (SQLException e) {
                log.info("error", e); // 위에서 예외터져도 catch로 잡아버리기 때문에 아래의 if 블록이 실행되면서 con.close() 호출됨
            }
        }

        if (con != null) {
            // tcp connection을 닫아야함, 안닫으면 계속 연결이 유지되면서 떠다님
            try {
                con.close();
            } catch (SQLException e) {
                log.info("error", e);
            }
        }
    }

    private Connection getConnection() {
        return DBConnectionUtil.getConnection();
    }

}

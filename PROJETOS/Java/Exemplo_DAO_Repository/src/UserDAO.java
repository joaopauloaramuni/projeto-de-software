public interface UserDAO {
    void save(User user);
    User findById(int id);
    void update(User user);
    void delete(int id);
}

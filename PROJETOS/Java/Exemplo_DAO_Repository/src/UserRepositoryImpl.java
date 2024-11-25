public class UserRepositoryImpl implements UserRepository {
    private UserDAO userDAO;

    public UserRepositoryImpl() {
        this.userDAO = new UserDAOImpl();
    }

    @Override
    public void addUser(User user) {
        userDAO.save(user);
    }

    @Override
    public User getUser(int id) {
        return userDAO.findById(id);
    }

    @Override
    public void updateUser(User user) {
        userDAO.update(user);
    }

    @Override
    public void removeUser(int id) {
        userDAO.delete(id);
    }
}

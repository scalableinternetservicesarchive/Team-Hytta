class AddUserToCabins < ActiveRecord::Migration
  def change
    add_reference :cabins, :user, index: true
  end
end

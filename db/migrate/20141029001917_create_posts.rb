class CreatePosts < ActiveRecord::Migration
  def change
    create_table :posts do |t|
      t.string :title
      t.text :message
      t.references :cabin, index: true

      t.timestamps
    end
  end
end

class Post < ActiveRecord::Base
  belongs_to :cabin
  #validates :title, presence: true
  validates :cabin, presence: true
end
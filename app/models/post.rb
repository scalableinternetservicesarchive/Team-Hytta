class Post < ActiveRecord::Base
  belongs_to :cabin
  has_many :comments
  #validates :title, presence: true
  validates :cabin, presence: true
end
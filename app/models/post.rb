class Post < ActiveRecord::Base
  belongs_to :cabin
  belongs_to :user
  has_many :comments, dependent: :destroy
  #validates :title, presence: true
  validates :cabin, presence: true
  validates :user, presence: true
end